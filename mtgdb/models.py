from django.db import models


class CardSet(models.Model):
    
    name = models.CharField(max_length=255)
    date = models.DateField()

class Card(models.Model):
    
    name = models.CharField(max_length=255)
    mana_cost = models.CharField(max_length=255, blank=True)

class CardPrinting(models.Model):
    
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE)
    