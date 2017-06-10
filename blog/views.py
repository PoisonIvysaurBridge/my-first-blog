from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import AuthorForm, PostForm
from .models import Post #, Author
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
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