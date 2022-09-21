from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.views import ListingViewSet, SpView

router = DefaultRouter()
router.register('listing', ListingViewSet, basename='listing')
router.register('sp', SpView, basename='sp')

urlpatterns = [
    path('home/', include(router.urls)),
]
