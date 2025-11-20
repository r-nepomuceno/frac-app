from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from classifieds import views

def health_check(request):
    return HttpResponse("ok")

urlpatterns = [
    path("", views.home, name="home"),  # Home page at root
    path("admin/", admin.site.urls),
    
    # Health check for monitoring
    path("health/", health_check, name="health"),

    # Executives (handled by classifieds/urls.py)
    path("executives/", include("classifieds.urls")),

    # Jobs (handled by classifieds/job_urls.py)
    path("jobs/", include("classifieds.job_urls")),
]