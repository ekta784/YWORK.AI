from rest_framework import serializers
from .models import Student   # your app's model

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emptable
        fields = '__all__'
