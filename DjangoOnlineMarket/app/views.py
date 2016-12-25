"""
Definition of views.
"""
from app.models import Category, Item, Comment
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib import auth
from app.forms import CommentForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,}
    )


def categories(request):
    """Renders the cat page."""
    all_categories = Category.objects.all()

    assert isinstance(request, HttpRequest)
    return render(request,'app/categories.html',{
        'all_categories': all_categories, 
        'year':datetime.now().year,}
    )
def category(request, id):
    """Renders the category page."""

    assert isinstance(request, HttpRequest)
    return render(request,'app/detail.html',{
            'category': Category.objects.get(id = id),
            'items': Item.objects.filter(category_id = id), 
            'year':datetime.now().year,}
    )
def item(request, id):
    """Renders the item page."""
    item = get_object_or_404(Item, id=id)
    assert isinstance(request, HttpRequest)

    form = CommentForm()
    if request.method == "POST":
       form = CommentForm(request.POST)
       if form.is_valid():
           if request.user.is_anonymous:
               return redirect('/auth/login/')
           comment = form.save(commit=False)
           comment.item_id = id
           comment.peson_name = request.user.username
           comment.save()
           return redirect('/categories/item/'+ comment.item_id) 
       else:
           form = CommentForm()

    return render(request,'app/item_detail.html',{
            'item': Item.objects.get(id = id),
            'comments': Comment.objects.filter(item_id = id), 
            'year':datetime.now().year,
            'form': form,}
    )

