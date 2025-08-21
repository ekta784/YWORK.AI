from rest_framework import serializers
from .models import Emptable

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emptable
        fields = '__all__'

