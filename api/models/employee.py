from django.db import models
from api.models import Company

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    about = models.TextField()
    position = models.CharField(max_length=100, choices=(
        ('Manager', 'manager'),
        ('Software Developer', 'sd'),
        ('Project Leader', 'pl')
    ))
    
    company_detail = models.ForeignKey(Company, on_delete=models.CASCADE)