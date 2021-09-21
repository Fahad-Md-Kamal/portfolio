from django.shortcuts import render
from .models import AboutMe, Education, Technology,Skill, TechFramework

def portfolioView(request):
    context = {
        'aboutme': AboutMe.objects.filter(is_active=True).first(),
        'eduations': Education.objects.all(),
        'skills':  Skill.objects.all(),
        'frameworks': TechFramework.objects.all(),

    }
    return render(request, 'portfolio/index.html', context)