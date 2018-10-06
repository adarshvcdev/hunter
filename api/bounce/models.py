from django.db import models

# Create your models here.

INDEX_CHOICES = (
        ('Nifty', 'Nifty'),
        ('Midcap', 'Midcap'),
        ('Smallcap', 'Smallcap'),
    )


class Scrip(models.Model):    
    ticker = models.CharField(max_length=255, null=False)    
    name = models.CharField(max_length=255, null=False)
    index = models.CharField(choices=INDEX_CHOICES, default='Nifty', max_length=100)

    class Meta:
        ordering = ('ticker',)