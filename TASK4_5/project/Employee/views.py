from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Emptable,Deptable
from .serializers import EmpSerializer,Emp_deptSerializer

class EmployeeView(APIView):

    def get(self, request):
        employees = Emptable.objects.all()
        serializer = EmpSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dep_view(APIView):
    def get(self, request):
        employees_dept = Deptable.objects.all()
        serializer = Emp_deptSerializer(employees_dept, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Emp_deptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)