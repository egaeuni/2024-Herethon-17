from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q, Count
from .models import Mento
# Create your views here.
def home(request):
    search_query = request.GET.get('search', '')
    sort = request.GET.get('sort', 'latest')
    
    mentos = Mento.objects.all()
    
    if search_query:
        mentos = mentos.filter(
            Q(name__icontains=search_query) | 
            Q(nickname__icontains=search_query) | 
            Q(tag__icontains=search_query) |
            Q(intro__icontains=search_query) |
            Q(content_1__icontains=search_query) |
            Q(content_2__icontains=search_query) |
            Q(content_3__icontains=search_query) |
            Q(content_4__icontains=search_query)
        )
    
    if sort == 'popular':
        mentos = mentos.annotate(popularity=Count('questions')).order_by('-popularity', '-id')
    else:
        mentos = mentos.order_by('-id')
    
    return render(request, 'mentoring/home.html', {'mentos': mentos, 'search_query': search_query, 'sort': sort})

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

def search(request):
    sort = request.GET.get('sort', 'latest')
    search = request.GET.get('search', '')
    
    if search:
        search_list = Mento.objects.filter(
            Q(name__icontains=search) | 
            Q(nickname__icontains=search) | 
            Q(tag__icontains=search) |
            Q(intro__icontains=search) |
            Q(content_1__icontains=search) |
            Q(content_2__icontains=search) |
            Q(content_3__icontains=search) |
            Q(content_4__icontains=search)
        )
    else:
        search_list = Mento.objects.all()

    return render(request, 'mentoring/search.html', {'search_list': search_list, 'sort': sort})


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


def sheet_list(request):
    records = Record.objects.all().order_by('-id')  #'-id': 역순으로 정렬
    return render(request, 'metoring/sheet_list.html', {'records': records})


