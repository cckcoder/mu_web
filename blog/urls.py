from django.urls import path
from .views import (
    home, about, post_details,
    contact
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("post-detail/<int:post_id>/", post_details, name="post-detail"),
    path("contact/", contact, name="contact")
]
