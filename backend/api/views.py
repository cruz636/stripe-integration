from rest_framework import generics

from stripe_integration.models import Item
from .serializers import ItemSerializer


class ItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DetailItemView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# todo: when creating an item, create it on Stripe to. And get the item's link
