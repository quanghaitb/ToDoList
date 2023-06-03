from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Job)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'level', 'degree_of_urgency', 'deadline', 'author')
    prepopulated_fields = {}
    
admin.site.register(models.Type)