from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


from .models import CustomUser
from django.views.generic.edit import FormView




class RegisterForm(UserCreationForm):
	
	class Meta:
		model = get_user_model()
		fields = ('email', 'username', 'password1', 'password2','tech_city', 'first_name', 'last_name') 



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')