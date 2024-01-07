from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'phone_number',
        'balance',
    ]

@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = [
        'customer',
        'total',
    ]