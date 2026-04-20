import requests
import re
from django.core.management.base import BaseCommand
from .models import WikidataContribution, WikidataPointRule, Contest, Participant

class Command(BaseCommand):
    help = 'Fetches and scores Wikidata contributions for active contests'

    def handle(self, *args, **options):
        contests = Contest.objects.filter(is_active=True)
        for contest in contests:
            participants = Participant.objects.filter(contest=contest)
            for participant in participants:
                self.audit_and_score(participant, contest)

    def audit_and_score(self, participant, contest):
        if not getattr(contest, 'wikidata_enabled', False):
            return 

        rules = WikidataPointRule.objects.filter(contest=contest)
        weights = {rule.action_type: rule.points for rule in rules} if rules.exists() else {'label': 2, 'description': 3, 'fact': 5, 'reference': 4, 'image': 5}
            
        api_url = "https://www.wikidata.org/w/api.php"
        params = {
            "action": "query", "list": "usercontribs", 
            "ucuser": participant.username,
            "ucstart": f"{contest.end_date}T23:59:59Z", "ucend": f"{contest.start_date}T00:00:00Z",
            "uclimit": "500", "ucprop": "comment|ids|flags|timestamp", "format": "json"
        }

        uccontinue = None
        while True:
            if uccontinue: params['uccontinue'] = uccontinue
            
            # I added a timeout=10 to handle API stability
            response = requests.get(api_url, params=params, timeout=10).json()
            edits = response.get('query', {}).get('usercontribs', [])

            for edit in edits:
                if getattr(contest, 'wikidata_exclude_bots', True) and 'bot' in edit:
                    continue

                comment = edit.get('comment', '')
                revid = edit.get('revid')
                
                # It will extract the Item ID (QID)
                item_match = re.search(r'Q\d+', comment)
                item_id = item_match.group(0) if item_match else None

                # It Linked-Only Mode Check
                if getattr(contest, 'wikidata_linked_only', False):
                    allowed_items = getattr(contest, 'target_qids', [])
                    if item_id not in allowed_items: continue

                is_pt = bool(re.search(r'\|pt(-br)?', comment))
                
                points, action = 0, "other"
                if 'P18' in comment: points, action = weights.get('image', 0), "Image (P18)"
                elif 'wbsetlabel' in comment: points, action = weights.get('label', 0), "Label"
                elif 'wbsetdescription' in comment: points, action = weights.get('description', 0), "Description"
                elif 'wbsetclaim-create' in comment: points, action = weights.get('fact', 0), "Statement/Fact"
                elif 'wbsetreference-add' in comment: points, action = weights.get('reference', 0), "Reference"

                # here saving the comment
                WikidataContribution.objects.update_or_create(
                    contest=contest, revid=revid,
                    defaults={
                        'participant': participant,
                        'item': item_id,
                        'comment': comment, # I added a Paper Trail
                        'timestamp': edit['timestamp'],
                        'is_portuguese': is_pt,
                        'action_type': action,
                        'points': points
                    }
                )

            if 'continue' in response and 'uccontinue' in response['continue']:
                uccontinue = response['continue']['uccontinue']
            else: break

        self.stdout.write(f"AUDIT_COMPLETE: {participant.username} synchronized.")
