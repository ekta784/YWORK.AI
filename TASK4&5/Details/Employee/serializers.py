from rest_framework import serializers
from .models import Student   # your app's model

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
