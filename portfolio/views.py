from django.shortcuts import render

# Create your views here.
# portfolio/views.py
from django.shortcuts import render
from .models import Profile, Project

def home(request):
    # get first profile or None
    profile = Profile.objects.first()
    projects = Project.objects.all().order_by('order')
    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'index.html', context)

