from rest_framework import generics
from .models import SupportingOrganization
from .serializers import SupportingOrganizationSerializer


class SupportingOrgCreateAPIView(generics.CreateAPIView):
    """ Это ед. вюшка принимающая POST запрос """
    queryset = SupportingOrganization.objects.all()
    serializer_class = SupportingOrganizationSerializer
    # permission_classes = [AllowAny]


class SupportingOrganizationListCreateView(generics.ListCreateAPIView):
    queryset = SupportingOrganization.objects.all()
    serializer_class = SupportingOrganizationSerializer


class SupportingOrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupportingOrganization.objects.all()
    serializer_class = SupportingOrganizationSerializer
