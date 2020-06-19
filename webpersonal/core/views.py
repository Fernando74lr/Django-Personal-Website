from django.shortcuts import render, HttpResponse

http_head = """
        <h1>My personal website</h1>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About me</a></li>
            <li><a href="/portfolio/">Porfolio</a></li>
            <li><a href="/contact/">Contact</a></li>
        </ul>
    """

def home(request):
    return HttpResponse(http_head + '<h2>Cover page</h2>')

def about(request):
    return HttpResponse(http_head +  '<h2>About me</h2><p>Hi, my name is Fernando</p>')

def portfolio(request):
    return HttpResponse(http_head +  '<h2>Portfolio</h2><p>Here you can see some of my projects</p>')

def contact(request):
    return HttpResponse(http_head +  '<h2>Contact</h2><p>Some info so you can get in touch with me</p>')