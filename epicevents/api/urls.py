from django.urls import path, include

from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from . import views

router = routers.SimpleRouter()
router.register('members', views.UserViewset, basename='members')

projects_router = NestedSimpleRouter(router, 'members', lookup='member')

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]
