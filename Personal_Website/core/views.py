from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def page(request):
    return render(request, 'core/page.html')
