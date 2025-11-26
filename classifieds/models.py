from django.conf import settings
from django.db import models


class ExecutiveProfile(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=160)
    bio = models.TextField(blank=True)
    skills_text = models.CharField(max_length=300, blank=True)  # Legacy field - keep for now
    rate_text = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    timezone = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Owner field for user authentication
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="executive_profiles",
        null=True,
        blank=True
    )
    
    # NEW: Tags field for matching
    skills_tags = models.CharField(
        max_length=500, 
        blank=True,
        help_text="Comma-separated tags (e.g., python, django, cto, startup)"
    )

    def __str__(self):
        return f"{self.name} — {self.title}"
    
    def get_tags_list(self):
        """Return tags as a cleaned list"""
        if not self.skills_tags:
            return []
        return [tag.strip().lower() for tag in self.skills_tags.split(",") if tag.strip()]


class Job(models.Model):
    title = models.CharField(max_length=160)
    company = models.CharField(max_length=160)
    description = models.TextField()
    duration_text = models.CharField(max_length=120, blank=True)
    budget_text = models.CharField(max_length=120, blank=True)
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    # Owner field
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="jobs"
    )
    
    # NEW: Tags field for matching
    required_skills_tags = models.CharField(
        max_length=500, 
        blank=True,
        help_text="Comma-separated tags (e.g., python, startup, remote)"
    )

    def __str__(self):
        return f"{self.title} — {self.company}"
    
    def get_tags_list(self):
        """Return tags as a cleaned list"""
        if not self.required_skills_tags:
            return []
        return [tag.strip().lower() for tag in self.required_skills_tags.split(",") if tag.strip()]