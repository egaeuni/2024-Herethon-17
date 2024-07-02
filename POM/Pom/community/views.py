from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    posts=Post.objects.all().order_by('-id')
    return render(request, 'community/list.html', {'posts':posts})

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title =title,
            content = content,
            author = request.user,
        )
        return redirect('community:list')
    return render(request, 'community/create.html')

@login_required
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'community/detail.html', {'post':post})

@login_required
def create_answer(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    if request.method == "POST":
        Answer.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post,
        )
        return redirect('community:detail', post_id)



@login_required
def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.add(request.user)
    return redirect('community:detail', post_id)

@login_required
def remove_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.remove(request.user)
    return redirect('community:detail', post_id)

@login_required
def add_scrap(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    post.scrap.add(request.user)
    return redirect('community:detail', post_id)

@login_required
def remove_scrap(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    post.scrap.remove(request.user)
    return redirect('community:detail', post_id)