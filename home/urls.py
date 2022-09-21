from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.views import ListingViewSet

router = DefaultRouter()
router.register('listing', ListingViewSet, basename='listing')

urlpatterns = [
    path('home/', include(router.urls)),
]
