from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import UserCreationForm, EmailOrUsernameModelBackend

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
                login(request,user)
                return redirect('/')
            else:
                user = EmailOrUsernameModelBackend.authenticate(request, email= username, password = password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                
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
                return redirect('/')

        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
