from django.db import models

class WikidataContribution(models.Model):
    """
    The permanent storage for Wikidata scores. 
    This is the 'Vault' that stores the math from logic.py.
    """
    # 🚨 ADDED THESE TWO BRIDGES (ForeignKeys) 🚨
    # This links your data directly to the existing WikiScore tables
    contest = models.ForeignKey('Contest', on_delete=models.CASCADE)
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    
    revid = models.BigIntegerField(unique=True)
    timestamp = models.DateTimeField()
    
    # logic of PT vs GL
    # This separates the 'Linguistic' work from the 'Global' technical work
    is_portuguese = models.BooleanField(default=False)
    
    # below is the categorization of the edit
    action_type = models.CharField(max_length=50) # Label, Description, Facts, etc.
    points = models.IntegerField(default=0)

    class Meta:
        # Updated to ensure uniqueness per contest, not just overall
        unique_together = ('contest', 'revid')
        verbose_name = "Wikidata Contribution"

    def __str__(self):
        return f"{self.participant.username} | {self.revid} | {self.points}pts"
