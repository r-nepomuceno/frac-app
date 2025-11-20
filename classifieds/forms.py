from django import forms
from .models import Job, ExecutiveProfile

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "company", "description", "duration_text", "budget_text", "contact_email"]
        labels = {
            "duration_text": "Duration (e.g., 8-12 weeks, 3-6 months)",
            "budget_text": "Budget (e.g., $5-8k/month, $150-200/hr)",
            "contact_email": "Contact Email",
        }

class ExecutiveProfileForm(forms.ModelForm):
    class Meta:
        model = ExecutiveProfile
        fields = ["name", "title", "bio", "skills_text", "rate_text", "email", "timezone"]
        labels = {
            "skills_text": "Skills (comma-separated)",
            "rate_text": "Rate (e.g., $150-200/hr)",
        }