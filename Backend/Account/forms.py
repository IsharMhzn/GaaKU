from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


batch_choices = [(i, i) for i in range(2012, 2021)]
department_choices = [
    ('chem', ('Department of Chemical Science and Engineering')),
    ('civil', ('Department of Civil Engineering')),
    ('comp', ('Department of Computer Science and Engineering')),
    ('mech', ('Department of Mechanical Engineering')),
    ('elec', ('Department of Electrical and Electronics Engineering')),
    ('geo', ('Department of Geomatics Engineering')),
]
semester_choices = [
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(help_text='First name')
    last_name = forms.CharField(help_text='Last name')
    email = forms.EmailField(help_text='Email address')
    dob = forms.DateField(help_text='Date of birth')
    batch = forms.IntegerField(widget=forms.Select(choices=batch_choices))
    department = forms.CharField(
        widget=forms.Select(choices=department_choices))
    group = forms.CharField()
    semester = forms.CharField(widget=forms.Select(choices=semester_choices))
    phone_no = forms.CharField()

    class meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',
                  'dob', 'batch', 'department', 'group', 'semester', 'phone_no')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
