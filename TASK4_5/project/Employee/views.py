from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Emptable
from .serializers import EmpSerializer

class EmployeeView(APIView):

    # GET - List all employees
    def get(self, request):
        employees = Emptable.objects.all()
        serializer = EmpSerializer(employees, many=True)
        return Response(serializer.data)

    # POST - Create new employee
    def post(self, request):
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
