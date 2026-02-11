from rest_framework import routers
from mtgdb.views import CardSetViewSet, CardViewSet, CardPrintingViewSet

from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'cardsets', CardSetViewSet)
router.register(r'cards', CardViewSet)
router.register(r'cardprintings', CardPrintingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
