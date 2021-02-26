from django.shortcuts import render 

# Create your views here.
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'



from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .backends import EmailSender

UserModel = get_user_model()
from .forms import RegisterForm
# 


def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            CustomUser = form.save(commit=False)
            CustomUser.is_active = False
            CustomUser.save()
        
            EmailSender.send_activation_email(request,CustomUser,form)
            
            return render(request,'accounts/confirm_emailuser.html')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login to your account.<a href="http://127.0.0.1:8000/accounts/login/"> <button>Login</button></a>')
    else:
        return HttpResponse('Activation link is invalid!')