import requests
import re
from django.core.management.base import BaseCommand
from .models import WikidataContribution, Contest, Participant

class Command(BaseCommand):
    help = 'Fetches and scores Wikidata contributions for active contests'

    def handle(self, *args, **options):
        # 1. It grabs all active contests from the system
        contests = Contest.objects.filter(is_active=True)
        
        for contest in contests:
            participants = Participant.objects.filter(contest=contest)
            for participant in participants:
                self.audit_and_score(participant, contest)

    def audit_and_score(self, participant, contest):
        # These are my exact weights
        weights = {'label': 2, 'description': 3, 'fact': 5, 'reference': 4, 'image': 5}
        api_url = "https://www.wikidata.org/w/api.php"

        params = {
            "action": "query",
            "list": "usercontribs",
            "ucuser": participant.username,
            "ucstart": f"{contest.end_date}T23:59:59Z",
            "ucend": f"{contest.start_date}T00:00:00Z",
            "uclimit": "500",
            "ucprop": "comment|ids|flags|timestamp",
            "format": "json"
        }

        response = requests.get(api_url, params=params).json()
        edits = response.get('query', {}).get('usercontribs', [])

        for edit in edits:
            # 1. Bot Shield
            if 'bot' in edit:
                continue

            comment = edit.get('comment', '')
            revid = edit.get('revid')
            
            # 2. PT Tag Check
            is_pt = bool(re.search(r'\|pt', comment))
            
            # 3. Here is the Action Matching
            points = 0
            action = "other"

            if 'P18' in comment:
                points, action = weights['image'], "Image (P18)"
            elif 'wbsetlabel' in comment:
                points, action = weights['label'], "Label"
            elif 'wbsetdescription' in comment:
                points, action = weights['description'], "Description"
            elif 'wbsetclaim-create' in comment:
                points, action = weights['fact'], "Statement/Fact"
            elif 'wbsetreference-add' in comment:
                points, action = weights['reference'], "Reference"

            # 4. it will save the data into the permanent record and link it to the sytem
            WikidataContribution.objects.update_or_create(
                contest=contest, # Link added
                revid=revid,
                defaults={
                    'participant': participant, # Link added
                    'timestamp': edit['timestamp'],
                    'is_portuguese': is_pt,
                    'action_type': action,
                    'points': points
                }
            )

        self.stdout.write(f"AUDIT_COMPLETE: {participant.username} records synchronized.")
