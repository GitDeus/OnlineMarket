from django.conf.urls import url 
import app.views
urlpatterns = [  
    url(r'^$', app.views.categories, name='categories'),
    url(r'^category/(?P<id>\d+)$', app.views.category, name='category'),
    url(r'^item/(?P<id>\d+)$', app.views.item, name='item'),
    ]