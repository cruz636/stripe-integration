from rest_framework.decorators import action
from stripe_integration.models import Item
from .serializers import ItemSerializer
from rest_framework import serializers, viewsets, response


class ItemViewSet(viewsets.ViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        return qs

    @action(methods="GET", url_path="items", detail=True)
    def get_items(self):
        return self.get_queryset()
