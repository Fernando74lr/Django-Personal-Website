from django.shortcuts import render
from .models import Project

def portfolio(request):
    # Return all the projects that has our model Project.
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects})
