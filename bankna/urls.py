"""
URL configuration for bankna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tanakarn import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home' ),
    path('login',views.loginPage, name='log-page'),
    path('homePage',views.homePage, name='home-page'),
    path('deposit',views.depositPage, name='depos-page'),
    path('withdraw',views.withdrawPage, name='with-page'),
    path('register',views.register, name='regis'),
    path('registermember',views.registerMember, name='regis-member'),
    path('loginuser',views.loginUser, name='log_user'),
    path('money',views.DepositMoney, name='get_money'),
    path('w_money',views.WithdrawMoney, name='los_money'),

    
]
