from django.urls import path
from .views import (
    home, about, post_details,
    contact, sign_up
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("post-detail/<int:post_id>/", post_details, name="post-detail"),
    path("contact/", contact, name="contact"),
    path("sign-up/", sign_up, name="sign-up")
]
