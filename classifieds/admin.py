from django.contrib import admin
from .models import ExecutiveProfile

@admin.register(ExecutiveProfile)
class ExecutiveProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "email", "rate_text", "created_at")
    search_fields = ("name", "title", "skills_text", "email")
