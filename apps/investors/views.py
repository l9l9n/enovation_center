from rest_framework import generics
from .models import Investor
from .serializers import InvestorSerializer


class InvestorCreateAPIView(generics.CreateAPIView):
    """ Это ед. вюшка принимающая POST запрос """
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    # permission_classes = [AllowAny]


class InvestorListCreateView(generics.ListCreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class InvestorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
