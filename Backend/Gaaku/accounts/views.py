from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from .forms import SignUpForm
from .tokens import account_activation_token

# Create your views here.
def signup_page_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.profile.first_name = form.cleaned_data.get('first_name')
            # user.profile.last_name = form.cleaned_data.get('last_name')
            # user.first_name = form.cleaned_data.get('first_name')
            # user.last_name = form.cleaned_data.get('last_name')
            # user.profile.email = form.cleaned_data.get('email')
            # user.email = form.cleaned_data.get('email')
            # user.profile.dob = form.cleaned_data.get('dob')
            # user.profile.batch = form.cleaned_data.get('batch')
            # user.profile.semester = form.cleaned_data.get('semester')
            # user.profile.phone_no = form.cleaned_data.get('phone_no')
            
            user.save()
            redirect('login')
            # current_site = get_current_site(request)
            # mail_subj = 'Confirm your GaaKU account'
            # message = render_to_string('accounts/account_activate_email.html', {
            #                         'user': user,
            #                         'domain': current_site.domain,
            #                         'uid': user.pk,
            #                         'token': account_activation_token.make_token(user),
            #                     })
            # to_email = user.profile.email
            # send_mail(mail_subj, message, settings.EMAIL_HOST_USER, [to_email])
            # return HttpResponse('The email has been sent. If not found please check your spam folder. Confirm your email address to complete the verification.')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def activate(request, uid, token):
    try:
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid.')

def login_page_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, 'Your username or password is incorrect.')
    return render(request, 'accounts/login.html', {})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')