from django.db import models

class Passage(models.Model):
    """
    A passage to be memorized, consisting of any number
    of paragraphs
    """
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Phrase(models.Model):
    """
    Phrases to memorize.
    """
    passage = models.ForeignKey(Passage)
    text = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.text
