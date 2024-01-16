from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from django.db.models import F


from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# หน้าโฮมเพจ --


@login_required()
def homePage (request): 
    user_username = request.user.username
    user = User.objects.get(username=user_username)
    customer = models.Customer.objects.get(user=user)

    transaction = models.Transaction.objects.filter(customer=customer).order_by('-id')

   
    return render (request, 'index.html',
                   {
                       "balance":customer.balance,
                        "number_phone":customer.phone_number,
                       "trans":transaction,
                       "trans_count":transaction.count(),
                       
                   })

# หน้าสมัครสมาชิก

def  registerMember(request):
    first_name = request.POST.get('f_name')
    last_name = request.POST.get('l_name')
    username = request.POST.get('username')
    password = request.POST.get('passw')
    pin = request.POST.get('pin_regis')
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
                pin=pin
            )
            if customer:
                return redirect("log-page")
    
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
        return render("regis")


def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user:
        login(request, user)
        return redirect("home-page")
    else:
        
        return redirect("log-page")
        

# logout --naja
    
def logout_view(request):
    logout(request,'login.html')



# หน้าล็อกอิน --
def loginPage (request):
    return render (request, 'login.html')

# ฝากเงิน --
login_required
def depositPage (request):

    user_username = request.user.username
    user = User.objects.get(username=user_username)
    customer = models.Customer.objects.get(user=user)


    transaction = models.Transaction.objects.filter(customer=customer).order_by('-id')
    

    return render (request, 'buttons.html',{
        "balance":customer.balance,
        "number_phone":customer.phone_number,
        "trans":transaction,
        "trans_count":transaction.count(   )
    })

# ถอนเงิน --
login_required
def withdrawPage (request):
    user_username = request.user.username
    user = User.objects.get(username=user_username)
    customer = models.Customer.objects.get(user=user)

    transaction = models.Transaction.objects.filter(customer=customer).order_by('-id')

    return render (request, 'cards.html',{
        "balance":customer.balance,
        "number_phone":customer.phone_number,
        "trans":transaction,
        "trans_count":transaction.count()
    })

# หน้าสมัครสมาชิก
def register (request):
    return render (request, 'register.html')


def DepositMoney (request):
    money=request.POST.get('money')
    
    user_username = request.user.username
    user = User.objects.get(username=user_username)
    customer = models.Customer.objects.get(user=user)


    models.Customer.objects.filter(user=user).update(balance=F("balance")+int(money))
    

    models.Transaction.objects.create(
        customer=customer,
        type=1,
        total=money
    )

    return redirect('depos-page')



def WithdrawMoney (request):
    money=request.POST.get('money')

    
    
    user_username = request.user.username
    user = User.objects.get(username=user_username)
    customer = models.Customer.objects.get(user=user)

    if int(money) < int(customer.balance):
            

        models.Customer.objects.filter(user=user).update(balance=F("balance")-int(money))
        
        models.Transaction.objects.create(
            customer=customer,
            type=-1,
            total=money
        )


    return redirect('with-page')



# def HomePage (request):
