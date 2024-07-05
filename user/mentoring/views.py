from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q, Count
from .models import Mento
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    mentos = Mento.objects.all()
    sort = request.GET.get('sort', 'latest')
    search = request.GET.get('search', '')

    if search:
        mentos = mentos.filter(
            Q(name__icontains=search) | 
            Q(nickname__icontains=search) | 
            Q(tag__icontains=search) |
            Q(intro__icontains=search) |
            Q(content_1__icontains=search) |
            Q(content_2__icontains=search) |
            Q(content_3__icontains=search) |
            Q(content_4__icontains=search)
        )
    
    if sort == 'popular':
        mentos = mentos.annotate(popularity=Count('questions')).order_by('-popularity', '-id')
    else:
        mentos = mentos.order_by('-id')
    
    return render(request, 'mentoring/home.html', {'mentos': mentos, 'search': search})

def detail(request, id):
    mento = get_object_or_404(Mento, id=id)
    return render(request, 'mentoring/detail.html', {'mento': mento})

def question(request, mento_id):
    mento = get_object_or_404(Mento, id=mento_id)
    if request.method == "POST":
        content = request.POST.get('content')

        question = Question.objects.create(content = content, mento=mento)
        question.save()
        return redirect('mentoring:question', mento_id)
    questions = Question.objects.filter(mento=mento)
    return render(request,'mentoring/question.html', {'mento': mento, 'questions': questions})

def record_sheet(request):
    if request.method == "POST":
        plan = request.POST.get('plan')
        advice = request.POST.get('advice')
        pledge = request.POST.get('pledge')

        record = Record.objects.create(
            plan = plan,
            advice = advice,
            pledge = pledge,
        )
        return redirect('mentoring:home')
    return render(request, 'mentoring/record_sheet.html')

@login_required
def create_comment(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    if request.method == "POST":
        content = request.POST.get('content')

        Comment.objects.create(
            content = content,
            question = question,
        )
        return redirect('mentoring:question', question_id)
    return render(request, 'mentoring/question.html')