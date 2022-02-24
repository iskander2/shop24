from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)


class EmailChangeForm(forms.Form):
    email = forms.EmailField()

class PasswordChangeForm(forms.Form):
    password = forms.CharField()