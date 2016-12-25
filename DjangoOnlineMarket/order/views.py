from django.shortcuts import render
from django.http import HttpRequest
from django.contrib import auth
from app.models import Category, Item
# Create your views here.

def order(request):
    """Renders the item page."""
    all_Items = Item.objects.all()
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
       if request.user.is_anonymous:
           return redirect('/auth/login/')
           
       return redirect('/order/') 

           


    return render(request, 'order/order.html',{'username': auth.get_user(request).username })