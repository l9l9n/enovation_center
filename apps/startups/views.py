from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Startup
from .serializers import StartupSerializer


class StartupListCreateView(generics.ListCreateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    # permission_classes = [AllowAny]


class StartupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    # permission_classes = [AllowAny]
