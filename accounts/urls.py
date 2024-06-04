from django.urls import path
from . import views

from accounts.views import ResetPasswordView
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    #login
    path('login/',views.login_view,name='login'),
    #logout
    path('logout/',views.logout_view,name='logout'),
    #registeration / signup
    path('signup/',views.signup_view,name='signup'),
    #reset password
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]