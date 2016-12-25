"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
import app.forms
import loginsys.views

urlpatterns = [
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

     url(r'^registration$',loginsys.views.RegistrationFormView.as_view(), name='registration'),

]
