from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from classifieds import views

def health_check(request):
    return HttpResponse("ok")

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    
    path("health/", health_check, name="health"),
    
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("executives/", include("classifieds.urls")),

    path("jobs/", include("classifieds.job_urls")),
]