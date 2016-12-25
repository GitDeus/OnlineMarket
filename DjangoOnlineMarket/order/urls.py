"""
Definition of urls for DjangoWebProject.
"""

from django.conf.urls import url, include

from django.conf.urls import url 
import order.views
urlpatterns = [
     url(r'^$',order.views.order, name='order'),

]
