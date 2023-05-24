from webbrowser import get
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import LoginForm,SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import UserModel
# from wallet.models import Wallet
from .models import *



# class Login(LoginView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'login.html',{})
class Signup(View):
    def get(self, request, *args, **kwargs):
        context ={}
        context['form'] = SignUpForm()
        return render(request, 'register.html',context)
        
    def post(self, request, *args, **kwargs):
        
            if request.method == 'POST':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    if not request.user.is_authenticated:
                        auth_login(request, user)
                        messages.success(self.request, "Account Created Successfully")
                        return HttpResponseRedirect(reverse('dashboard'))
                        

                    else:
                        context ={'current_path':"Add User"}
                        context['form'] = SignUpForm()
                        messages.success(self.request, "user successfully added")
                        return render(request, 'add_user.html',context)
                    
                else:
                    if not request.user.is_authenticated:
                        context = {'form':form}
                        return render(request, 'register.html',context)
                    else:
                        context = {'form':form}
                        return render(request, 'add_user.html',context)
                        
            else:
                return HttpResponseRedirect(reverse('register') )

    




class LoginPage(LoginView):
    
    
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        from django.contrib.auth.models import User
        context ={}
        context['form'] = LoginForm()
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        print(request.POST['username'])
        print(request.POST['password'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else: 
            messages.error(request, 'Incorrect username or password')
        return HttpResponseRedirect(reverse('login'))