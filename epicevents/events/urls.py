from django.urls import path, include

from rest_framework import routers

from events.views import EventViewset
router = routers.SimpleRouter()
router.register('', EventViewset, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]
