from django.contrib import admin

# Register your models here.
# portfolio/admin.py
from django.contrib import admin
from .models import Profile, Project

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'order')
    ordering = ('order',)
