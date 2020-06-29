"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

# Extended configuration so we can serve media files.
if settings.DEBUG:
    # 'static' allow us to serve static files.
    from django.conf.urls.static import static
    # Add the path to the media file
    # static(path_where_we_want_to_ser_the_media_files, the_root_where_it_has_to_look_for_the_media_files)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)