from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from store.models import Product


batch_choices = [(i, i) for i in range(2012, 2021)]
department_choices = [
    ('chem', 'Department of Chemical Science and Engineering'),
    ('civil', 'Department of Civil Engineering'),
    ('comp', 'Department of Computer Science and Engineering'),
    ('mech', 'Department of Mechanical Engineering'),
    ('elec', 'Department of Electrical and Electronics Engineering'),
    ('geo', 'Department of Geomatics Engineering'),
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

category_choices = [
    ('Electronics', 'Electronics'),
    ('Homes and Furnitures', 'Homes and Furnitures'),
    ('Sports', 'Sports'),
    ('Education Materials', 'Education Materials'),
    ('Other Accessories', 'Other Accessories'),
]

negotiation_choices = [
    (1, 'Unknown'),
    (2, 'Yes'),
    (3, 'No')
]

urgent_choices = [
    (1, 'Yes'),
    (2, 'No')
]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(help_text='First name')
    last_name = forms.CharField(help_text='Last name')
    email = forms.EmailField(help_text='Email address')
    dob = forms.DateField(help_text='Date of birth', widget=forms.TextInput(attrs={'placeholder': 'Format: YYYY-MM-DD'}))
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


class ProductForm(forms.ModelForm):
    name = forms.CharField(help_text="Product name")
    category = forms.CharField(widget=forms.Select(choices=category_choices))
    price = forms.IntegerField(help_text="Price")
    description = forms.CharField(help_text="Description")
    # negotiation = forms.BooleanField(widget=forms.Select(choices=negotiation_choices

    img = forms.ImageField(help_text="Product Image")
    contact_info = forms.CharField(help_text="Contact Info.")
    # urgent = forms.BooleanField(help_text="Urgent?", widget=forms.Select(choices=urgent_choices
    #                                                                      ))

    class Meta:
        model = Product
        fields = ['name', 'category', 'price',
                  'description', 'negotiation', 'img', 'contact_info', 'urgent']
