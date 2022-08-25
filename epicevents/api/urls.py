from django.urls import path, include

from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from api.views import index, UserViewset, ClientViewset, ContractViewset, EventViewset

router = routers.SimpleRouter()
router.register('members', UserViewset, basename='members')
router.register('clients', ClientViewset, basename='clients')

clients_router = NestedSimpleRouter(router, 'clients', lookup='client')
clients_router.register('contracts', ContractViewset,
                        basename='clients-contracts')

contracts_router = NestedSimpleRouter(
    clients_router, 'contracts', lookup='contract')
contracts_router.register('event', EventViewset,
                          basename='clients-contracts-event')

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('', include(clients_router.urls)),
    path('', include(contracts_router.urls)),
]
