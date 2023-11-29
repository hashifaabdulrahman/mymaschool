from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Student
from .forms import Studentform

# Create your views here.
def home(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('studentlogin')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                print("user created")
        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('login')
    return render(request,'register.html')
def contact(request):
    return render(request,'contact.html')
def studentlogin(request):
    if request.method == "POST":
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=Studentform()
    dict_form={
        'form':form
    }
    return render(request,'studentlogin.html',dict_form)
def logout(request):
    return render(request,'index.html')