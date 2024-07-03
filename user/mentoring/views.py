from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
    mentos = Mento.objects.all()
    return render(request, 'mentoring/home.html', {'mentos':mentos})

def detail(request, id):
    mento = get_object_or_404(Mento, id=id)
    return render(request, 'mentoring/detail.html', {'mento': mento})

def question(request, mento_id):
    mento = get_object_or_404(Mento, id=mento_id)
    if request.method == "POST":
        content = request.POST.get('content')

        question = Question.objects.create(content = content)
        question.save()
        return redirect('mentoring:question', mento_id)
    questions = Question.objects.filter(mento=mento)
    return render(request,'mentoring/question.html', {'mento': mento, 'questions': questions})

def search(request):
    mento_list = Mento.objects.all()
    search = request.GET.get('search', '')
    if search:
        search_list = mento_list.filter(
            Q(name__icontains=search) | 
            Q(nickname__icontains=search) | 
            Q(tag__icontains=search) |
            Q(intro__icontains=search) |
            Q(content__icontains=search)
        )
    else:
        search_list = mento_list

    return render(request, 'mentoring/search.html', {'search_list': search_list})

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


