from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            request.session['username'] = request.POST['username']
            request.session['password1'] = request.POST['password1']
            return redirect('signup_child')
    return render(request, 'signup.html')

def signup_child(request):
    if request.method == "POST":
        username = request.session['username']
        password = request.session['password1']
        gender = request.POST['gender']
        birth_date_str = request.POST['birth_date']
        
        # 출생일 문자열을 datetime.date 객체로 변환
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()

        # 사용자 생성
        user = User.objects.create_user(username, password=password)

        # 프로필 생성 및 연결
        profile = Profile(user=user, gender=gender, birth_date=birth_date)
        profile.save()

        auth.login(request, user)
        return redirect('home')
    return render(request, 'signup_child.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})
    return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return redirect('home')

def home(request):  
    return render(request, 'home.html')

def mypage(request):
    if request.user.is_authenticated:
        # 사용자의 프로필 정보 가져오기
        try:
            profile = Profile.objects.get(user=request.user)
            birth_date = profile.birth_date
            gender = profile.gender

            # 출생일로부터 현재까지 몇 개월인지 계산
            current_age_months = calculate_age_in_months(birth_date)

            return render(request, 'mypage.html', {
                'username': request.user.username,
                'gender': gender,
                'current_age_months': current_age_months  # 변수명 수정
            })
        except Profile.DoesNotExist:
            return render(request, 'mypage.html', {
                'username': request.user.username,
                'gender': '미정',
                'current_age_months': '알 수 없음'  # 변수명 수정
            })
    else:
        return redirect('login')  # 로그인 페이지로 리다이렉트

def calculate_age_in_months(birth_date):
    today = date.today()
    delta = relativedelta(today, birth_date)
    
    years = delta.years
    months = delta.months
    
    if years == 0:
        if months == 0:
            return '방금 태어남'
        elif months == 1:
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



