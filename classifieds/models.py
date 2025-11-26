from django.conf import settings
from django.db import models


class ExecutiveProfile(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=160)
    bio = models.TextField(blank=True)
    
    # Location (replacing timezone)
    location = models.CharField(
        max_length=100, 
        blank=True,
        help_text="City, State/Region (e.g., San Francisco, CA)"
    )
    
    # Rate - numeric with implied $/hour
    hourly_rate = models.PositiveIntegerField(
        null=True, 
        blank=True,
        help_text="Your hourly rate in USD"
    )
    
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Owner field for user authentication
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="executive_profiles",
        null=True,
        blank=True
    )
    
    # Tags field for matching
    skills_tags = models.CharField(
        max_length=500, 
        blank=True,
        help_text="Comma-separated skills (e.g., finance, strategy, fundraising)"
    )

    def __str__(self):
        return f"{self.name} — {self.title}"
    
    def get_tags_list(self):
        """Return tags as a cleaned list"""
        if not self.skills_tags:
            return []
        return [tag.strip().lower() for tag in self.skills_tags.split(",") if tag.strip()]
    
    @property
    def rate_display(self):
        """Display rate as $X/hour"""
        if self.hourly_rate:
            return f"${self.hourly_rate}/hour"
        return None


class Opportunity(models.Model):
    """Job/Opportunity posting (renamed from Job for consistency)"""
    
    BUDGET_PERIOD_CHOICES = [
        ('hour', 'per hour'),
        ('day', 'per day'),
        ('week', 'per week'),
        ('month', 'per month'),
    ]
    
    DURATION_PERIOD_CHOICES = [
        ('days', 'days'),
        ('weeks', 'weeks'),
        ('months', 'months'),
    ]
    
    title = models.CharField(max_length=160)
    company = models.CharField(max_length=160)
    description = models.TextField()
    
    # Budget - numeric + period dropdown
    budget_amount = models.PositiveIntegerField(
        null=True, 
        blank=True,
        help_text="Budget amount in USD"
    )
    budget_period = models.CharField(
        max_length=20, 
        choices=BUDGET_PERIOD_CHOICES, 
        default='month',
        blank=True
    )
    
    # Duration - numeric + period dropdown
    duration_amount = models.PositiveIntegerField(
        null=True, 
        blank=True,
        help_text="Expected duration"
    )
    duration_period = models.CharField(
        max_length=20, 
        choices=DURATION_PERIOD_CHOICES, 
        default='months',
        blank=True
    )
    
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    # Owner field
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="opportunities"
    )
    
    # Tags field for matching
    required_skills_tags = models.CharField(
        max_length=500, 
        blank=True,
        help_text="Comma-separated required skills (e.g., finance, strategy, fundraising)"
    )

    class Meta:
        verbose_name_plural = "Opportunities"

    def __str__(self):
        return f"{self.title} — {self.company}"
    
    def get_tags_list(self):
        """Return tags as a cleaned list"""
        if not self.required_skills_tags:
            return []
        return [tag.strip().lower() for tag in self.required_skills_tags.split(",") if tag.strip()]
    
    @property
    def budget_display(self):
        """Display budget as $X/period"""
        if self.budget_amount:
            period_display = dict(self.BUDGET_PERIOD_CHOICES).get(self.budget_period, self.budget_period)
            return f"${self.budget_amount:,} {period_display}"
        return None
    
    @property
    def duration_display(self):
        """Display duration as X period"""
        if self.duration_amount:
            return f"{self.duration_amount} {self.duration_period}"
        return None


# Keep Job as an alias for backward compatibility during migration
Job = Opportunity