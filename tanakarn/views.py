from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import authenticate, login

# Create your views here.

# หน้าโฮมเพจ --
def homePage (request): 
   
    return render (request, 'index.html')

def registerMember(request):
    first_name = request.POST.get('f_name')
    last_name = request.POST.get('l_name')
    username = request.POST.get('username')
    password = request.POST.get('passw')
    print(first_name, last_name, username, password)
    try :

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

        if (user):
            customer = models.Customer.objects.create(
                user=user,
                phone_number="-",
                addres="-",
                balance=0.00,
                pin="111111"
            )
            if customer:
                return redirect("home")
    
    except :
        return redirect("regis")



# login __ซ้ำซาก__
    

def loginMember(request):
    username = request.POST.get('User_n')
    password = request.POST.get('passwo')

    try :

        user = User.objects.create_user(
            username = username,
            password = password,
        )

        if (user):
            customer = models.Customer.objects.create(
                user=user,
                phone_number="-",
                addres="-",
                balance=0.00,
                pin="111111"
            )
            if customer:
                return redirect("home")
    
    except :
        return redirect("regis")


def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user.is_active:
        login(request, user)
        return redirect("homrpage")
    else:
        
        return redirect("login")
        



# หน้าล็อกอิน --
def loginPage (request):
    return render (request, 'login.html')

# ฝากเงิน --
def depositPage (request):
    return render (request, 'buttons.html')

# ถอนเงิน --
def withdrawPage (request):
    return render (request, 'cards.html')

# หน้าสมัครสมาชิก
def register (request):
    return render (request, 'register.html')

