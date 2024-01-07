from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 

Transaction_Type = (
    (-1, "Withdraw"),
    (1, "Deposit")
)


class Customer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    addres = models.TextField()
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    pin = models.CharField(max_length=6)

    def __str__(self):

        return self.user.first_name+" "+self.user.last_name
    

class Transaction (models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    type = models.IntegerField(choices=Transaction_Type)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    create = models.DateTimeField(auto_now_add=True)

    