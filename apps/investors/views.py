from rest_framework import generics
from .models import Investor
from .serializers import InvestorSerializer


class InvestorListCreateView(generics.ListCreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class InvestorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
