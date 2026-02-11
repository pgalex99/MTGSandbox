from rest_framework import serializers
from mtgdb.models import Card, CardSet, CardPrinting

class CardSetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CardSet
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = '__all__'
        
class CardPrintingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CardPrinting
        fields = '__all__'