from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor, HospitalStay

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(HospitalStay)