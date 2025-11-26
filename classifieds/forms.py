from django import forms
from .models import ExecutiveProfile, Job


class ExecutiveProfileForm(forms.ModelForm):
    class Meta:
        model = ExecutiveProfile
        fields = [
            "name",
            "title",
            "bio",
            "skills_text",
            "skills_tags",  # NEW: Tags field
            "rate_text",
            "email",
            "timezone",
        ]
        labels = {
            "name": "Full Name",
            "title": "Professional Title",
            "bio": "Bio / About",
            "skills_text": "Skills Description",
            "skills_tags": "Skills Tags",  # NEW
            "rate_text": "Rate (e.g., $150-200/hr)",
            "email": "Contact Email",
            "timezone": "Timezone",
        }
        help_texts = {
            "skills_tags": "Enter skills separated by commas (e.g., python, django, cto, startup leadership)",
        }
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
            "skills_tags": forms.TextInput(attrs={"placeholder": "python, django, cto, startup"}),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "company",
            "description",
            "duration_text",
            "budget_text",
            "required_skills_tags",  # NEW: Tags field
            "contact_email",
        ]
        labels = {
            "title": "Job Title",
            "company": "Company Name",
            "description": "Job Description",
            "duration_text": "Duration (e.g., 3-6 months, ongoing)",
            "budget_text": "Budget (e.g., $10k-15k/month)",
            "required_skills_tags": "Required Skills",  # NEW
            "contact_email": "Contact Email",
        }
        help_texts = {
            "required_skills_tags": "Enter required skills separated by commas (e.g., python, startup experience, remote)",
        }
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "required_skills_tags": forms.TextInput(attrs={"placeholder": "python, startup, remote, leadership"}),
        }