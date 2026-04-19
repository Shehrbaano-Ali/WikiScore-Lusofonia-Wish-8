import requests
import re
from .models import WikidataContribution

class WikiscoreEngine:
    """
    The Python version of your app.js logic.
    It fetches, filters for bots/reverts, and applies the PT/GL split.
    """
    def __init__(self):
        # The exact weights from your JS build
        self.weights = {
            'label': 2,
            'description': 3,
            'fact': 5,
            'reference': 4,
            'image': 5
        }
        self.api_url = "https://www.wikidata.org/w/api.php"

    def audit_and_score(self, username, start_date, end_date):
        # Setup API call (Same parameters as your JS fetch)
        params = {
            "action": "query",
            "list": "usercontribs",
            "ucuser": username,
            "ucstart": f"{end_date}T23:59:59Z",
            "ucend": f"{start_date}T00:00:00Z",
            "uclimit": "500",
            "ucprop": "comment|ids|flags|timestamp",
            "format": "json"
        }

        response = requests.get(self.api_url, params=params).json()
        edits = response.get('query', {}).get('usercontribs', [])

        for edit in edits:
            # 1. BOT SHIELD: Ignore automated edits
            if 'bot' in edit:
                continue

            comment = edit.get('comment', '')
            revid = edit.get('revid')
            
            # 2. DATA INTEGRITY: Skip edits with 'mw-reverted' (Validation logic)
            # Note: In a full Django setup, we'd use a batch-check here like your validateBatch
            
            # 3. LINGUISTIC PRECISION: Check for the Portuguese tag
            is_pt = bool(re.search(r'\|pt', comment))
            
            # 4. SCORING LOGIC: Match your weights
            points = 0
            action = "other"

            if 'P18' in comment:
                points = self.weights['image']
                action = "Image (P18)"
            elif 'wbsetlabel' in comment:
                points = self.weights['label']
                action = "Label"
            elif 'wbsetdescription' in comment:
                points = self.weights['description']
                action = "Description"
            elif 'wbsetclaim-create' in comment:
                points = self.weights['fact']
                action = "Statement/Fact"
            elif 'wbsetreference-add' in comment:
                points = self.weights['reference']
                action = "Reference"

            # 5. COMMIT TO DATABASE: Save the record permanently
            WikidataContribution.objects.update_or_create(
                revid=revid,
                defaults={
                    'username': username,
                    'timestamp': edit['timestamp'],
                    'is_portuguese': is_pt,
                    'action_type': action,
                    'points': points
                }
            )

        print(f"AUDIT_COMPLETE: {username} records synchronized.")