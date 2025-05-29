from django import forms
from bv1.models import ContactModel, SignUP


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone', 'message']


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUP
        fields = ['email']