from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="job_list"),                  # /jobs/
    path("post/", views.post_job, name="post_job"),             # /jobs/post/
    path("<int:pk>/", views.job_detail, name="job_detail"),     # /jobs/1/
    path("<int:pk>/edit/", views.edit_job, name="edit_job"),    # NEW: /jobs/1/edit/
]
