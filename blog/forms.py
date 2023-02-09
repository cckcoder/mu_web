from django.forms import ModelForm, TextInput, EmailInput, Textarea, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["subject", "sender", "email", "detail"]

        widgets = {
            "subject": TextInput(attrs={"class": "form-control col-sm-8"}),
            "sender": TextInput(attrs={"class": "form-control col-sm-8"}),
            "email": EmailInput(attrs={"class": "form-control col-sm-8"}),
            "detail": Textarea(attrs={"class": "form-control col-sm-8"})
        }


class RegisterForm(UserCreationForm):
    email = EmailField()
    model = User
    fields = [
        "username",
        "email",
        "password1",
        "password2",
    ]