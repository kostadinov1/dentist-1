from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from dentist_2_project.services.models import Service, BlogPost


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
