from django.forms import ModelForm, TextInput, EmailInput, Textarea
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