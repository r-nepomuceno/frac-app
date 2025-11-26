from django import forms
from .models import ExecutiveProfile, Opportunity


class ExecutiveProfileForm(forms.ModelForm):
    """Form for creating/editing executive profiles"""
    
    class Meta:
        model = ExecutiveProfile
        fields = [
            'name',
            'title', 
            'bio',
            'location',
            'hourly_rate',
            'skills_tags',
            'email',
        ]
        labels = {
            'name': 'Full Name',
            'title': 'Professional Title',
            'bio': 'About / Bio',
            'location': 'Location',
            'hourly_rate': 'Hourly Rate (USD)',
            'skills_tags': 'Skills',
            'email': 'Contact Email',
        }
        help_texts = {
            'location': 'City, State/Region (e.g., San Francisco, CA)',
            'hourly_rate': 'Your rate will be displayed as $/hour',
            'skills_tags': 'Comma-separated skills (e.g., finance, strategy, fundraising, operations)',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Jane Smith'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Fractional CFO'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': 'Tell us about your background and expertise...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'San Francisco, CA'
            }),
            'hourly_rate': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '250',
                'min': 0,
            }),
            'skills_tags': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'finance, strategy, fundraising, operations'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'jane@example.com'
            }),
        }


class OpportunityForm(forms.ModelForm):
    """Form for creating/editing opportunities"""
    
    class Meta:
        model = Opportunity
        fields = [
            'title',
            'company',
            'description',
            'budget_amount',
            'budget_period',
            'duration_amount',
            'duration_period',
            'required_skills_tags',
            'contact_email',
        ]
        labels = {
            'title': 'Opportunity Title',
            'company': 'Company Name',
            'description': 'Description',
            'budget_amount': 'Budget',
            'budget_period': 'Budget Period',
            'duration_amount': 'Duration',
            'duration_period': 'Duration Period',
            'required_skills_tags': 'Required Skills',
            'contact_email': 'Contact Email',
        }
        help_texts = {
            'description': 'Describe the role, responsibilities, and what you\'re looking for',
            'required_skills_tags': 'Comma-separated skills (e.g., finance, strategy, fundraising)',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Fractional CFO'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Acme Corp'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': 'We\'re looking for an experienced financial leader to help us...'
            }),
            'budget_amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '10000',
                'min': 0,
            }),
            'budget_period': forms.Select(attrs={
                'class': 'form-input',
            }),
            'duration_amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '3',
                'min': 0,
            }),
            'duration_period': forms.Select(attrs={
                'class': 'form-input',
            }),
            'required_skills_tags': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'finance, strategy, fundraising'
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'hiring@acmecorp.com'
            }),
        }


# Legacy alias for backward compatibility
JobForm = OpportunityForm