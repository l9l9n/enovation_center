from rest_framework import serializers
from .models import Startup


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ('name',
                  'description',
                  'industry',
                  'prototype_status',
                  'development_stage',
                  'development_stage',
                  'additional_files',
                  'contacts',
                  )
