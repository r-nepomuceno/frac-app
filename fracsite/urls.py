from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Executive directory
    path("executives/", include("classifieds.urls")),

    # Job board
    path("jobs/", include("classifieds.job_urls")),
]