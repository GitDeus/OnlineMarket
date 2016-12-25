from django.db import models
from app.models import Item
from django.utils.timezone import now


class MyManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(MyManager, self).all(*args, **kwargs)
        qs = qs_main.filter(order_name)
        return qs

class Order(models.Model):
    class Meta:
        db_table = 'Order'


    first_name = models.CharField(max_length=50, default='first name')
    last_name = models.CharField(max_length=50,default='last name')
    email = models.EmailField(max_length=50,default='email@email.com')
    address =  models.CharField(max_length=250, default='')
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=False, default=now)
    updated = models.DateTimeField(auto_now=False, default=now)
    paid = models.BooleanField(default=False)



    def __str__(self):
        return 'Order: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Item)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity