from rest_framework import serializers
from .models import Emptable,Deptable

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emptable
        fields = '__all__'

class Emp_deptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deptable
        fields = '__all__'