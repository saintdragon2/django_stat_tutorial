from django.contrib import admin
from .models import Organization, Dataset
# Register your models here.


admin.site.register(Dataset)
admin.site.register(Organization)