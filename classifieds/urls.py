from django.urls import path
from . import views

urlpatterns = [
    path("", views.exec_list, name="exec_list"),                      # /executives/
    path("create/", views.create_profile, name="create_profile"),     # /executives/create/
    path("<int:pk>/", views.exec_detail, name="exec_detail"),         # /executives/1/
    path("<int:pk>/edit/", views.edit_profile, name="edit_profile"),  # NEW: /executives/1/edit/
]