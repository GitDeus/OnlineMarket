
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import Comment


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class CommentForm(forms.ModelForm):

    content = forms.CharField(max_length=254,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': 'Text',
                                   'rows': '4'}))

    dignity = forms.CharField(max_length=254,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': 'Dignity',  'rows': '1'}))

    limitations = forms.CharField(max_length=254,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': 'Limitations',  'rows': '1'}))

    class Meta:
        model = Comment
        fields = ('content', 'dignity', 'limitations',)