from django.contrib import admin

from app.models import Category, Item, Comment
#from app.models import Item
#from app.models import Comment

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Comment)