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
