from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Post, Answer
from accounts.views import calculate_age_in_months  # 함수 가져오기
from django.db.models import Count
from .models import Post, Answer, ScrapCommunity
from accounts.views import calculate_age_in_months

@login_required
def list(request):
    sort = request.GET.get('sort', 'latest')
    
    if sort == 'popular':
        posts = Post.objects.all().annotate(popularity= Count('like')).order_by('-popularity', '-id')
    else:
        posts = Post.objects.all().order_by('-id')
    
    for post in posts:
        post.author.profile.current_age_months = calculate_age_in_months(post.author.profile.birth_date)
    
    return render(request, 'community/list.html', {'posts': posts})

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,  # 현재 로그인된 사용자
        )
        return redirect('community:list')
    return render(request, 'community/create.html')

@login_required
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    author_profile = post.author.profile
    nickname = author_profile.nickname
    birth_date = author_profile.birth_date  # 생일 정보 가져오기
    current_age_months = calculate_age_in_months(birth_date)  # 함수 사용

    return render(request, 'community/detail.html', {
        'post': post,
        'author_nickname': nickname,
        'author_current_age_months': current_age_months,
    })

@login_required
def create_answer(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        Answer.objects.create(
            content=request.POST.get('content'),
            author=request.user,  # 현재 로그인된 사용자
            post=post,
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
    post = get_object_or_404(Post, id=post_id)
    post.scrap.add(request.user)
    return redirect('community:detail', post_id)

@login_required
def remove_scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.scrap.remove(request.user)
    return redirect('community:detail', post_id)

@login_required
def delete(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('community:list')

@login_required
def delete_answer(request, answer_id):
    answer= get_object_or_404(Answer, id = answer_id)
    post_id = answer.post.id
    answer.delete()
    return redirect('community:detail', post_id)
