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
    
    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    
    # Two-path landing pages
    path("for-startups/", views.for_startups, name="for_startups"),
    path("for-fractionals/", views.for_fractionals, name="for_fractionals"),
    
    # A/B Test endpoint (MANDATORY for Sprint 4)
    # URL computed from sha1("restless-sound")[:7] = "b77952e"
    path("b77952e/", views.ab_test, name="ab_test"),

    # Executives
    path("executives/", include("classifieds.urls")),

    # Opportunities (renamed from Jobs)
    path("opportunities/", include("classifieds.opportunity_urls")),
    
    # Delete actions
    path("profile/<int:pk>/delete/", views.delete_profile, name="delete_profile"),
    path("opportunity/<int:pk>/delete/", views.delete_opportunity, name="delete_opportunity"),
    
    # Legacy redirect: /jobs/ -> /opportunities/
    path("jobs/", views.redirect_jobs_to_opportunities, name="jobs_redirect"),
]