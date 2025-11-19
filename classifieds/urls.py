from django.urls import path
from . import views

urlpatterns = [
    path("", views.exec_list, name="exec_list"),
    path("<int:pk>/", views.exec_detail, name="exec_detail"),
]

path("jobs/", views.job_list, name="job_list"),
path("jobs/new/", views.post_job, name="post_job"),