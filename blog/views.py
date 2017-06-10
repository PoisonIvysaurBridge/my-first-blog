from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import AuthorForm
from .models import Post #, Author
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
'''
def index(request):
    
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
            author.save()
            redirect('index')
    else:
        form = AuthorForm()
    return render(request,'index.html',{'AuthorForm' : form})
'''        