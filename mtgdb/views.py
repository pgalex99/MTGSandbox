from rest_framework import viewsets
from api.models import Card, CardSet, CardPrinting
from api.serializers import CardSerializer, CardSetSerializer, CardPrintingSerializer


class CardSetViewSet(viewsets.ModelViewSet):
    queryset = CardSet.objects.all()
    serializer_class = CardSetSerializer
    
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
class CardPrintingViewSet(viewsets.ModelViewSet):
    queryset = CardPrinting.objects.all()
    serializer_class = CardPrintingSerializer
    