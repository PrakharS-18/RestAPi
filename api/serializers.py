from rest_framework import serializers
from api.models.company import Company
from api.models.employee import Employee

class CompanySerializers(serializers.HyperlinkedModelSerializer):

    # only for  reading the company_id we can't edit this
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"  