from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('<h1>My personal website</h1><h2>Cover page</h2>')