from django.shortcuts import render
from rest_framework import viewsets
from api.models.company import Company
from api.models.employee import Employee
from api.serializers import CompanySerializers
from api.serializers import EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    # working url will be companies/<id>/employees
    # important to employee for a certain company
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company_detail = company)
        emps_serializer = EmployeeSerializer(emps, many=True, context= {'request':request})
        return Response(emps_serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
