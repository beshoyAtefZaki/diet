# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Patient ,MealsTFR,PatientTFR ,DoctorProfile
# Register your models here.
admin.site.register(Patient)
admin.site.register(MealsTFR)
admin.site.register(PatientTFR)
admin.site.register(DoctorProfile)