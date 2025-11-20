from django.urls import path
from . import views

urlpatterns = [
    path("", views.exec_list, name="exec_list"),
    path("<int:pk>/", views.exec_detail, name="exec_detail"),
]
