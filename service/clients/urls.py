from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientsView


router = DefaultRouter()
router.register('clients', ClientsView, basename='clients')

urlpatterns = [
    path('', include(router.urls)),    
]

