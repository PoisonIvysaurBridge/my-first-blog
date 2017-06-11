from django import forms
from .models import *
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)
    '''
    title = forms.CharField(label="Title:", max_length=100)
    text = forms.CharField(label="Content:")
'''
class AuthorForm(forms.Form):
    name = forms.CharField(label="User Name", max_length=100)
    pw = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username',)
    
    password = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)