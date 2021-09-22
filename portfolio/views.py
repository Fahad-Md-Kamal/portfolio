from django.shortcuts import render
from .models import AboutMe, Education, Technology,Skill, Platform, Project

def portfolioView(request):
    context = {
        'aboutme': AboutMe.objects.filter(is_active=True).first(),
        'eduations': Education.objects.all(),
        'skills':  Skill.objects.all(),
        'technologies': Technology.objects.all(),
        'platforms': Platform.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio/index.html', context)