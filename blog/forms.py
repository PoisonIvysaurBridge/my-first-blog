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
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
