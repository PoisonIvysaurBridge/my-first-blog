from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import *
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_sort(request):
    if request.method == "POST":
        if request.POST['sort']=="author":
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('author')
        elif request.POST['sort']=="title":
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('title')
        elif request.POST['sort']=="new":
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        elif request.POST['sort']=="old":
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        else:
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_filter(request):
    posts=[]
    
    if request.method == "POST":
        keyword = request.POST['search'].upper()
        filterby = request.POST['filterby']
        unfiltered = Post.objects.all()
        if(filterby == "author"):
            for i in unfiltered:
                if (i.author.username.upper().find(keyword) > -1):
                    posts.append(i)
        elif (filterby == "title"):
            for i in unfiltered:
                if (i.title.upper().find(keyword) > -1):
                    posts.append(i)
        elif (filterby == "text"):
            for i in unfiltered:
                if (i.text.upper().find(keyword) > -1):
                    posts.append(i)
        else:
            for i in unfiltered:
                if (i.author.username.upper().find(keyword) > -1 or
                    i.title.upper().find(keyword) > -1 or
                    i.text.upper().find(keyword) > -1):
                    posts.append(i)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def register(request):
    if request.method == "POST":
        #form = AuthorForm(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            #login(new_user,new_user.password)
            # redirect, or however you want to get to the main view
            return redirect('login')
            '''
            user = User(username=form.cleaned_data['name'], password=form.cleaned_data['pw'])
            user.save()
            author = Author(name=form.cleaned_data['name'], pw=form.cleaned_data['pw'])
            author.save()
            return redirect('login')'''
    else:
        form = UserForm()
    return render(request,'registration/register.html',{'UserForm' : form})
   
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
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