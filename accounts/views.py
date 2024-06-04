from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import UserCreationForm, EmailOrUsernameModelBackend

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

import sweetify


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # username = request.POST['username']
            # password = request.POST['password']
            # form = AuthenticationForm(request,data=request.POST)
            # if form.is_valid():
            #     username = form.cleaned_data.get('username')
            #     password = form.cleaned_data.get('password')

            #     user = authenticate(request, username=username, password=password)

            #     if user is not None:
            #         login(request, user)
            #         return redirect('/')
            
            username = request.POST['username']
            password = request.POST['password']

            user = EmailOrUsernameModelBackend.authenticate(request, username=username, password=password)
            if user is not None:
                sweetify.success(request,'Great!',text='login succesfully.', persistent='ok', type='success',timer=2000)
                login(request,user)
                return redirect('/')
            else:
                    # Base method with no type specified
                sweetify.error(request,'Oops...',text='wrong username or email ntered. - reload the site', persistent='close', type='error')
                return render(request,'accounts/login.html')

                
        # form = AuthenticationForm()
        # context = {'form':form}
        return render(request,'accounts/login.html')
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
    # if request.user.is_authenticated:
    #     logout(request)
    # return redirect('/')    

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                # return redirect('accounts/login/')
                sweetify.success(request,'signup succesfully!',text='now you can login to your account.', persistent='ok', type='success',timer=2000)
                return redirect('/')
            sweetify.success(request,'signup succesfully!',text='now you can login to your account.', persistent='ok', type='success',timer=2000)

        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('accounts:login')