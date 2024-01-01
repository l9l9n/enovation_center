from rest_framework import serializers
from .models import SupportingOrganization


class SupportingOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportingOrganization
        fields = '__all__'
