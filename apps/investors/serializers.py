from rest_framework import serializers
from .models import Investor


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('name',
                  'investment_area',
                  'investment_size',
                  'additional_files',
                  'contacts',
                  )
