from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from . models import banner,review
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib import auth
@csrf_exempt

# Create your views here.
def fun1(request):
    obj=banner.objects.all()
    obj1=review.objects.all()
    return render(request,"index.html",{'result':obj,"feed":obj1})
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invaild credantialis")
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        user=request.POST['user']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass']
        conpass=request.POST['conpass']
        print("this reached")
        if password==conpass:
            if User.objects.filter(username=user).exists():
                messages.info(request,"username taken")
                print("user")
                return redirect('register')
            else:
                us1=User.objects.create_user(username=user,password=password,first_name=fname,last_name=lname)
                print("lll1")
                us1.save()

                print("created sucess")
        else:
            messages.info(request,"password dont match ")
            return redirect('register')
    else:
        # return redirect('fun1')
        pass
    return render(request,"reg.html")
def logout(request):
    auth.logout(request)
    return redirect("/")