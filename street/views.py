from rest_framework.viewsets import ModelViewSet

from .models import Home, Street
from .serializer import HomeSerializer, StreetSerializer


class StreetViews(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer 


class HomeViews(ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer