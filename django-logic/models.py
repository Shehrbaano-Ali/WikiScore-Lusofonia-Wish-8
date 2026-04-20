from django.db import models

class WikidataPointRule(models.Model):
    """
    Allows organizers to change points directly from the Django Admin panel.
    """
    # I Linked point rules to the existing contest
    contest = models.ForeignKey('Contest', on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50) # Label, Description, Fact, etc.
    points = models.IntegerField(default=0)

    class Meta:
        unique_together = ('contest', 'action_type')
        verbose_name = "Wikidata Point Rule"

    def __str__(self):
        return f"{self.contest.name} | {self.action_type}: {self.points}pts"

class WikidataContribution(models.Model):
    """
    The 'Vault' that stores the audit trail and score for every edit.
    """
    contest = models.ForeignKey('Contest', on_delete=models.CASCADE)
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    
    # I used a BigInteger for safety against massive Wikidata revision IDs
    revid = models.BigIntegerField(unique=True)
    item = models.CharField(max_length=20, null=True, blank=True) 
    
    # I used a raw audit trail for transparency
    comment = models.TextField(blank=True, default='') 
    timestamp = models.DateTimeField()
    
    is_portuguese = models.BooleanField(default=False)
    action_type = models.CharField(max_length=50) 
    points = models.IntegerField(default=0)

    class Meta:
        unique_together = ('contest', 'revid')
        verbose_name = "Wikidata Contribution"

    def __str__(self):
        return f"{self.participant.username} | {self.item} | {self.points}pts"
