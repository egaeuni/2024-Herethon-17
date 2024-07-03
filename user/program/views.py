from django.shortcuts import render
from .models import Program, Policy

def program_home(request):
    programs = Program.objects.all()[:6]
    policies = Policy.objects.all()[:3]  
    return render(request, 'program/program_home.html', {'programs': programs, 'policies': policies})

def program_list(request):
    query = request.GET.get('q', '')
    region = request.GET.get('region', '')
    
    programs = Program.objects.all()
    
    if query:
        programs = programs.filter(title__icontains=query)
    
    if region:
        programs = programs.filter(region=region)

    return render(request, 'program/program_list.html', {'programs': programs, 'query': query, 'region': region})

def policy_list(request):
    policies = Policy.objects.all()
    return render(request, 'program/policy_list.html', {'policies': policies})
