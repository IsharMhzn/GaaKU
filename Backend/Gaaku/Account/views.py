from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

from .models import Profile
from .forms import SignUpForm
from . import mail

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
            mail.send(domain = domain, userid=uid, email=user.email, type='confirm')
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

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user is not None:
            uid = (int(user.pk) + 945) * 556535
            mail.send(domain = get_current_site(request), userid=uid, email=user.email, type='reset')
            return HttpResponse('Please check your email to complete your registration. Kindly check your spam if needed.')
        else:
            messages.add_message(request, messages.INFO, 'This email is not registered.')
    else:
        return render(request, 'accounts/forgot_password.html')


def password_reset(request, userid):
    if request.method == 'POST':
        uid = int(userid) / 556535 - 945
        user = User.objects.get(pk=uid)
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            user.password = make_password(p1, salt=None, hasher='default')
            user.save()
            messages.add_message(request, messages.INFO, 'Your password has been updated.')
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, 'Please match both the passwords.')
    else:
        return render(request, 'accounts/password_reset.html')

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