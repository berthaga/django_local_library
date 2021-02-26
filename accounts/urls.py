from django.urls import path
from . import views
from accounts.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.urls import path,include 

urlpatterns = [
	
	path('login/', LoginView.as_view(), name='login'),
	path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/',PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('', include('django.contrib.auth.urls')),
    path('register/', views.signup, name="register"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'), 
]

