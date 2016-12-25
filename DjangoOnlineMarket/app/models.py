"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Person(models.Model):
    class Meta():
        db_table = 'person'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)



class Category(models.Model):
    class Meta():
        db_table = 'category'
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Item(models.Model):
    class Meta():
        db_table = 'item'
    item_name = models.CharField(max_length=30)
    item_price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class Comment(models.Model):
    class Meta():
        db_table = 'comment'

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    peson_name = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    approved_comment = models.BooleanField(default=False)
    dignity = models.CharField(max_length=200)
    limitations = models.CharField(max_length=200)

    comment_date = models.DateField(auto_now=True)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return  self.content



