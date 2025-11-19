from django.db import models

class ExecutiveProfile(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=160)
    bio = models.TextField(blank=True)
    skills_text = models.CharField(max_length=300, blank=True)  # comma-separated
    rate_text = models.CharField(max_length=120, blank=True)    # e.g., "$150–200/hr"
    email = models.EmailField()
    timezone = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.title}"

from django.conf import settings
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=160)
    company = models.CharField(max_length=160)
    description = models.TextField()                  # renamed from description_text
    duration_text = models.CharField(max_length=120, blank=True)  # e.g., "8–12 weeks"
    budget_text = models.CharField(max_length=120, blank=True)    # e.g., "$5–8k/mo"
    contact_email = models.EmailField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="jobs"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} — {self.company}"

