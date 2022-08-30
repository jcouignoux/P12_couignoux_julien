from django.urls import path, include

from rest_framework import routers
from staff.views import UserViewset

router = routers.SimpleRouter()
router.register('', UserViewset, basename='staff')

urlpatterns = [
    path('', include(router.urls)),
]
