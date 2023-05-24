from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from my_app.models import UserModel
from django.core.validators import RegexValidator

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    price = models.FloatField()
    stock = models.IntegerField()
    imageUrl = models.CharField(max_length=2500)
    

class Cart(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product_id = models.IntegerField(max_length=100, null=False,default=0)
    unit_price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    total_purchase = models.IntegerField(null=False)
    date_of_update = models.DateField(null=False)