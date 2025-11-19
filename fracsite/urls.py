from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Executives (handled by classifieds/urls.py)
    path("executives/", include("classifieds.urls")),

    # Jobs (handled by classifieds/job_urls.py)
    path("jobs/", include("classifieds.urls")),

    # Healthcheck
    path("health/", include("health_check.urls")),
]
