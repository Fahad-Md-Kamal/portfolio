from django.shortcuts import render
from .models import AboutMe, Education, Email, Technology,Skill, Platform, Project, Profile, OtherURLS, Contacts

def portfolioView(request):
    profile = Profile.objects.all().first()
    context = {
        'aboutme': AboutMe.objects.filter(is_active=True).first(),
        'eduations': Education.objects.all(),
        'skills':  Skill.objects.all(),
        'technologies': Technology.objects.all(),
        'platforms': Platform.objects.all(),
        'projects': Project.objects.all(),
        'profile': profile,
        'contacts': Contacts.objects.filter(user=profile),
        'emails': Email.objects.filter(user=profile),
        'links': OtherURLS.objects.filter(profile=profile)
    }
    return render(request, 'portfolio/index.html', context)