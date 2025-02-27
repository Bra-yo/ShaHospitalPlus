from django.contrib import admin
from HospitalApp.models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Staff)
admin.site.register(Ward)