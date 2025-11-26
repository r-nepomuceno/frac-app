from django.urls import path
from . import views

urlpatterns = [
    path("", views.opportunity_list, name="opportunity_list"),                      # /opportunities/
    path("post/", views.post_opportunity, name="post_opportunity"),                 # /opportunities/post/
    path("<int:pk>/", views.opportunity_detail, name="opportunity_detail"),         # /opportunities/1/
    path("<int:pk>/edit/", views.edit_opportunity, name="edit_opportunity"),        # /opportunities/1/edit/
]