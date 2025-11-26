from django.contrib import admin
from .models import ExecutiveProfile, Opportunity


@admin.register(ExecutiveProfile)
class ExecutiveProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "email", "hourly_rate", "location", "created_at")
    search_fields = ("name", "title", "skills_tags", "email", "location")
    list_filter = ("created_at",)


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "contact_email", "budget_amount", "budget_period", "is_active", "created_at")
    search_fields = ("title", "company", "description", "required_skills_tags")
    list_filter = ("is_active", "created_at", "budget_period")