from django.db import models

class WikidataContribution(models.Model):
    """
    The permanent storage for Wikidata scores. 
    This is the 'Vault' that stores the math from logic.py.
    """
    username = models.CharField(max_length=255)
    revid = models.BigIntegerField(unique=True)
    timestamp = models.DateTimeField()
    
    # logic of PT vs GL
    # This separates the 'Linguistic' work from the 'Global' technical work
    is_portuguese = models.BooleanField(default=False)
    
    # below is the categorization of the edit
    action_type = models.CharField(max_length=50) # Label, Description, Facts, etc.
    points = models.IntegerField(default=0)

    class Meta:
        # this ensures we never double count the same edit for the same user
        unique_together = ('username', 'revid')
        verbose_name = "Wikidata Contribution"

    def __str__(self):
        return f"{self.username} | {self.revid} | {self.points}pts"
