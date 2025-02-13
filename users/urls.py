from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, ProfileView, email_verification, UserPasswordResetView, ErrorUserPasswordReset

app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset-password'),
    path('error-reset-password/', ErrorUserPasswordReset.as_view(), name='error-reset-password'),

]