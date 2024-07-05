from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Program, Policy, Scrap

def program_home(request):
    programs = Program.objects.all()[:6]
    policies = Policy.objects.annotate(scrap_count=Count('scraps')).order_by('-created_at')[:3]
    return render(request, 'program/program_home.html', {'programs': programs, 'policies': policies})

def program_list(request):
    query = request.GET.get('q', '')
    region = request.GET.get('region', '')

    programs = Program.objects.annotate(scrap_count=Count('scraps'))

    if query:
        programs = programs.filter(title__icontains=query)

    if region:
        programs = programs.filter(region=region)

    return render(request, 'program/program_list.html', {'programs': programs, 'query': query, 'region': region})

def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    is_scrapped = Scrap.objects.filter(user=request.user, program=program).exists() if request.user.is_authenticated else False
    return render(request, 'program/program_detail.html', {'program': program, 'is_scrapped': is_scrapped})

def policy_list(request):
    sort_by = request.GET.get('sort_by', 'created_at')
    query = request.GET.get('q', '')

    policies = Policy.objects.annotate(scrap_count=Count('scraps'))

    if query:
        policies = policies.filter(title__icontains=query)

    if sort_by == 'scrap_count':
        policies = policies.order_by('-scrap_count', '-created_at')
    else:
        policies = policies.order_by('-created_at')

    return render(request, 'program/policy_list.html', {'policies': policies, 'sort_by': sort_by, 'query': query})

def policy_detail(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    is_scrapped = Scrap.objects.filter(user=request.user, policy=policy).exists() if request.user.is_authenticated else False
    return render(request, 'program/policy_detail.html', {'policy': policy, 'is_scrapped': is_scrapped})

@login_required
def add_scrap_policy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    Scrap.objects.get_or_create(user=request.user, policy=policy)
    return redirect('program:policy_detail', policy_id=policy_id)

@login_required
def remove_scrap_policy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    Scrap.objects.filter(user=request.user, policy=policy).delete()
    return redirect('program:policy_detail', policy_id=policy_id)

@login_required
def add_scrap_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    Scrap.objects.get_or_create(user=request.user, program=program)
    return redirect('program:program_detail', program_id=program_id)

@login_required
def remove_scrap_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    Scrap.objects.filter(user=request.user, program=program).delete()
    return redirect('program:program_detail', program_id=program_id)
