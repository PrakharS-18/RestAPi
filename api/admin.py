from django.contrib import admin
from api.models.company import Company

class AdminCompany(admin.ModelAdmin):
    list_display = ['name', 'company_id', 'locations']


# Register your models here.

admin.site.register(Company, AdminCompany)
