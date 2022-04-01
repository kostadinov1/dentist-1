from django.contrib import admin

# Register your models here.
from dentist_2_project.core.models import Appointment, Review


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass