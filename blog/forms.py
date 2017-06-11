from django import forms
from .models import Post
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
    pw = forms.CharField(label="Password", widget=forms.PasswordInput)
