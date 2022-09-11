import re
from django.shortcuts import render,redirect
from . form import Userform
from . models import User,Artical
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def like(request,no):
    artical=Artical.objects.get(id=no)
    artical.likes.add(request.user)
    likes=Artical.total_likes()
    return redirect('home')
def home(request):
    artical=Artical.objects.all()
    
    context={'context':artical}
    return render(request,'home.html',context)

def loginuser(request):
    Userf=Userform()
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            
            return render(request,'login.html',{'error':"wrong",'form':Userf})
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':"wrong",'form':Userf})
    
    return render(request,'login.html',{'form':Userf})

def logoutuser(request):
    logout(request)
    return redirect('home')

