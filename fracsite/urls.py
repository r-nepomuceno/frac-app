from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from classifieds import views

def health_check(request):
    return HttpResponse("ok")

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    
    # Health check
    path("health/", health_check, name="health"),
    
    # Authentication
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    
    # NEW: Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # Executives
    path("executives/", include("classifieds.urls")),

    # Jobs
    path("jobs/", include("classifieds.job_urls")),
]