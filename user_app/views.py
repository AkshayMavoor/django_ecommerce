
from multiprocessing import context
from django.shortcuts import render , redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from my_app.models import UserModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UpdateUser as UpdateUserForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied



# from .forms import InputForm


# Create your views here.


# def home_view(request):
#     context ={}
#     context['form']= InputForm()
#     return render(request, "home.html", context)
@method_decorator(login_required,name='dispatch')
class Dashboard(View):
    def get(self, request, *args, **kwargs):
        id=request.user.pk
    
        

        if not request.user.is_superuser:
            
            
        
           
            context = {'current_path':"Dashboard" ,"rank":"current_rank" , "next_rank":"next_rank"}
        else:

            context = {'current_path':"Dashboard" ,"rank":"current_rank" , "next_rank":"next_rank"}

        return render(request, 'home/dashboard.html',context)


@method_decorator(login_required,name='dispatch')
class Manage_user(View):
    def get(self, request, *args, **kwargs):
        user= UserModel.objects.filter(is_superuser=False).order_by('id')
        return render(request, 'home/manage_user.html',{'current_path':"Manage user" , 'users':user , 'ranks':"ranks"})



        return render(request, 'home/bonus_history.html',{ 'current_path':"Bonus History","datas":datas})
@method_decorator(login_required,name='dispatch')
class UpdateUser(View):
    def get(self, request,id, *args, **kwargs):
        user= UserModel.objects.get(id=id)
        if user.is_active:
            user.is_active=False
            user.save()
        else:
            user.is_active = True
            user.save()
        # print(users)
        return redirect('manage_user')


@method_decorator(login_required,name='dispatch')
class Error404(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/page-404.html',{})
@method_decorator(login_required,name='dispatch')
class Error403(View):
    def get(self, request, *args, **kwargs):
        raise PermissionDenied()






@method_decorator(login_required,name='dispatch')
class Profile(View):
    def get(self, request, *args, **kwargs):
        context = {'current_path':"Profile"}
        context['form'] = UpdateUserForm(initial={'first_name':request.user.first_name,'last_name':request.user.last_name,'username':request.user,'email':request.user.email})
        return render(request, 'home/profile.html', context)
        
