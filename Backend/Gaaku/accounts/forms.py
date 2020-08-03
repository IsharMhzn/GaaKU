from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Email Address')
    first_name = forms.CharField(max_length=50, help_text='First Name')
    last_name = forms.CharField(max_length=50, help_text='Last Name')
    dob = forms.DateField(help_text='Date of birth')
    # batch = forms.IntegerField()
    # department = forms.CharField()
    # semester = forms.IntegerField()
    # group = forms.CharField()
    # phone_no = forms.IntegerField()

    class meta:
        model = User
        field = ('first_name', 'last_name', 'email', 'dob', 'password1', 'password2',)
