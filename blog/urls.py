from django.urls import path
from .views import (
<<<<<<< HEAD
    home, about, post_detail, contact,
    thank_page, search, sign_up, sign_in,
    sign_out
=======
    home, about, post_details,
    contact
>>>>>>> c73505a9e006b131e7a0dcfc8f97fd9878230b9c
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
<<<<<<< HEAD
    path("post-detail/<int:post_id>", post_detail, name="post-detail"),
    path("contact/", contact, name="contact"),
    path("thanks/", thank_page, name="thanks"),
    path("search", search, name="search"),
    path("sign-up", sign_up, name="sign-up"),
    path("sign-in", sign_in, name="sign-in"),
    path("sign-out", sign_out, name="sign-out"),
]
=======
    path("post-detail/<int:post_id>/", post_details, name="post-detail"),
    path("contact/", contact, name="contact")
]
>>>>>>> c73505a9e006b131e7a0dcfc8f97fd9878230b9c
