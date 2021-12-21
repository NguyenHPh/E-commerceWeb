from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from products.models import Product
import uuid
from djongo import models


class Order(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "Order"

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    trayQuantity = models.IntegerField()
    trayPricePer = models.FloatField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        db_table = "OrderItem"