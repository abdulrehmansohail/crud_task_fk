from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from home.models import Listing
from home.serializers import ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]
    queryset = Listing.objects.all()

    def get_queryset(self):
        return self.queryset
