from django.shortcuts import render
from .models import Project #import the portfolio database

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html',{'projects':projects}) #passing the database object into the template
