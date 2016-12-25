# Create your views here.
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.base import View

from django.views.decorators.csrf import csrf_protect

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

        return user


class RegistrationFormView(View):
    form_class = MyRegistrationForm
    template_name = 'loginsys/registration.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    self.form_class = form
             
        return render(request,self.template_name,{'form':form})          


#def registration(request):
#    if request.method == 'POST':
#        form = RegistrationForm(request.POST)
#        if form.is_valid():
#            user = User.objects.create_user(username=form.cleaned_data['username'],
#            password=form.cleaned_data['password1'],
#            email=form.cleaned_data['email'])
#            return redirect('/auth/registration')
#    else:
#        form = RegistrationForm()

 
#    return  render(request,
#    'loginsys/registration.html',
#    {'form': form})
