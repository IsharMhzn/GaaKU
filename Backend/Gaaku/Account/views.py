from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Profile
from .forms import SignUpForm
from . import confirm_mail

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_active = False
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.dob = form.cleaned_data.get('dob')
            user.profile.batch = form.cleaned_data.get('batch')
            user.profile.department = form.cleaned_data.get('department')
            user.profile.group = form.cleaned_data.get('group')
            user.profile.semester = form.cleaned_data.get('semester')
            user.profile.phone_no = form.cleaned_data.get('phone_no')
            user.save()
            domain = get_current_site(request)
            uid = (int(user.pk) + 325) * 556535
            confirm_mail.send(domain = domain, userid=uid, email=user.email)
            return HttpResponse('Please check your email to complete your registration. Kindly check your spam if needed.')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, 'The username or password you entered is incorrect.')
    return render(request, 'accounts/login.html', {})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

def activate(request, userid):
    userid = int(userid) / 556535 - 325
    try:
        user = User.objects.get(pk=userid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:
        user.is_active = True
        user.save()
        messages.add_message(request, messages.INFO, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')