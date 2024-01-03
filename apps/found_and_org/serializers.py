from rest_framework import serializers
from .models import SupportingOrganization


class SupportingOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportingOrganization
        fields = ('name',
                  'support_type',
                  'support_conditions',
                  'additional_files',
                  'contacts',
                  )
