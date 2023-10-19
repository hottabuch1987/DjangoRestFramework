from django.shortcuts import render
from .models import User
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ClientsSerializer


class ClientsView(ReadOnlyModelViewSet):
    """clients"""
    queryset = User.objects.all()
    serializer_class = ClientsSerializer
