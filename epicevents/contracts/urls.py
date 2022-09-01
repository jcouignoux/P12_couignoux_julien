from django.urls import path, include

from rest_framework import routers

from contracts.views import ContractViewset

router = routers.SimpleRouter()
router.register('', ContractViewset, basename='contracts')

urlpatterns = [
    path('', include(router.urls)),
]
