from django.urls import path
from .views import (
    home, about, post_details, contact,
    sign_up, sign_in, sign_out
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("post-detail/<int:post_id>/", post_details, name="post-detail"),
    path("contact/", contact, name="contact"),
    path("sign-up/", sign_up, name="sign-up"),
    path("sign-in/", sign_in, name="sign-in"),
    path("sign-out/", sign_out, name="sign-out")
]
