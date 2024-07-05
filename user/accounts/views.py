from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from .models import Profile
from .forms import ProfileForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from community.models import Post, ScrapCommunity  
from program.models import Scrap, Policy, Program
from mentoring.models import Question, Record
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            request.session['username'] = request.POST['username']
            request.session['password1'] = request.POST['password1']
            request.session['nickname'] = request.POST['nickname']  # 닉네임 추가
            return redirect('accounts:signup_child')
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    return render(request, 'accounts/signup.html')

def signup_child(request):
    if request.method == "POST":
        username = request.session['username']
        password = request.session['password1']
        nickname = request.session['nickname']  # 닉네임 가져오기
        gender = request.POST['gender']
        birth_date_str = request.POST['birth_date']
        
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        user = User.objects.create_user(username, password=password)
        profile = Profile(user=user, gender=gender, birth_date=birth_date, nickname=nickname)
        profile.save()
        auth.login(request, user)
        return redirect('accounts:home')
    return render(request, 'accounts/signup_child.html')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, birth_date=date(2000, 1, 1), gender='Unknown', nickname='User')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance, birth_date=date(2000, 1, 1), gender='Unknown', nickname='User')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # 프로필이 없으면 생성
            Profile.objects.get_or_create(user=user, defaults={'birth_date': date(2000, 1, 1), 'gender': 'Unknown', 'nickname': 'User'})
            return redirect('accounts:home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('accounts:login')

def home(request):  
    return render(request, 'accounts/home.html')

@login_required
def mypage(request):
    if request.user.is_authenticated:
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user, birth_date=date(2000, 1, 1), gender='Unknown', nickname='User')

        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                return redirect('accounts:mypage')
        else:
            form = ProfileForm(instance=request.user.profile)
        
        try:
            profile = Profile.objects.get(user=request.user)
            birth_date = profile.birth_date
            gender = profile.gender
            nickname = profile.nickname

            # 작성한 게시글과 스크랩한 게시글 가져오기
            user_posts = Post.objects.filter(author=request.user)
            scrapped_posts = ScrapCommunity.objects.filter(user=request.user, post__isnull=False).select_related('post')
            scrapped_policies = Scrap.objects.filter(user=request.user, policy__isnull=False).select_related('policy')
            scrapped_programs = Scrap.objects.filter(user=request.user, program__isnull=False).select_related('program')

            # 멘토링 질문과 기록지 가져오기
            user_questions = Question.objects.filter(user=request.user)
            user_records = Record.objects.filter(user=request.user)

            # 스크랩 수의 합 계산
            total_scraps = scrapped_posts.count() + scrapped_policies.count() + scrapped_programs.count()

            # 출생일로부터 현재까지 몇 개월인지 계산
            current_age_months = calculate_age_in_months(birth_date)

            return render(request, 'accounts/mypage.html', {
                'nickname': nickname,
                'gender': gender,
                'current_age_months': current_age_months,
                'profile_pic_url': profile.profile_pic.url if profile.profile_pic else None,
                'form': form,
                'user_posts': user_posts,
                'scraped_posts': scrapped_posts,
                'scraped_policies': scrapped_policies,
                'scraped_programs': scrapped_programs,
                'scrapped_posts_count': scrapped_posts.count(),
                'scrapped_policies_count': scrapped_policies.count(),
                'scrapped_programs_count': scrapped_programs.count(),
                'user_questions': user_questions,
                'user_records': user_records,
                'total_scraps': total_scraps,  # 총 스크랩 수를 템플릿에 전달
            })
        except Profile.DoesNotExist:
            return render(request, 'accounts/mypage.html', {
                'nickname': 'Unknown',
                'gender': '미정',
                'current_age_months': '알 수 없음',
                'profile_pic_url': None,
                'form': form,
                'user_posts': [],
                'scraped_posts': [],
                'scraped_policies': [],
                'scraped_programs': [],
                'total_scraps': 0,  # 스크랩 수의 기본값을 0으로 설정
                'user_questions': [],
                'user_records': [],
            })
    else:
        return redirect('accounts:login')

def calculate_age_in_months(birth_date):
    today = date.today()
    delta = relativedelta(today, birth_date)
    
    years = delta.years
    months = delta.months
    
    if years == 0:
        if months == 1:
            return '1개월'
        else:
            return f'{months}개월'
    elif years == 1:
        if months == 0:
            return '1년'
        elif months == 1:
            return '1년 1개월'
        else:
            return f'1년 {months}개월'
    else:
        if months == 0:
            return f'{years}년'
        elif months == 1:
            return f'{years}년 1개월'
        else:
            return f'{years}년 {months}개월'

@login_required
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                return redirect('accounts:mypage')
        else:
            form = ProfileForm(instance=request.user.profile)
        
        return render(request, 'accounts/edit_profile.html', {
            'form': form,
            'profile_pic_url': request.user.profile.profile_pic.url if request.user.profile.profile_pic else None
        })
    else:
        return redirect('accounts:login')

@login_required
def post_number(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'mypage/post_number.html', {'user_posts': user_posts})

@login_required
def scrap_post(request):
    scrapped_posts = ScrapCommunity.objects.filter(user=request.user, post__isnull=False).select_related('post')
    return render(request, 'mypage/scrap_post.html', {'scrapped_posts': scrapped_posts})

@login_required
def scrap_policy(request):
    scrapped_policies = Scrap.objects.filter(user=request.user, policy__isnull=False).select_related('policy')
    return render(request, 'mypage/scrap_policy.html', {'scrapped_policies': scrapped_policies})

@login_required
def scrap_program(request):
    user = request.user
    scrapped_programs = Scrap.objects.filter(user=user, program__isnull=False).select_related('program')
    return render(request, 'mypage/scrap_program.html', {'scrapped_programs': scrapped_programs})

@login_required
def user_question(request):
    user_questions = Question.objects.filter(user=request.user)
    return render(request, 'mentoring/user_question.html', {'user_questions': user_questions})

@login_required
def user_record(request):
    user_records = Record.objects.filter(user=request.user)
    return render(request, 'mentoring/user_record.html', {'user_records': user_records})
