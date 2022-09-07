from django.urls import path, include

from rest_framework import routers

from clients.views import ClientViewset

router = routers.SimpleRouter()
router.register('', ClientViewset, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]
