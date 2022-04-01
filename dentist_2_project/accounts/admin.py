from django.contrib import admin

# Register your models here.
from dentist_2_project.accounts.models import AppUser, Profile


@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
