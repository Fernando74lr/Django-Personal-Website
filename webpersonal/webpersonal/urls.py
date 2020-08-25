from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views

from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about-me/', core_views.about, name='about'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', core_views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

# Extended configuration so we can serve media files.
if settings.DEBUG:
    # 'static' allow us to serve static files.
    from django.conf.urls.static import static
    # Add the path to the media file
    # static(path_where_we_want_to_ser_the_media_files, the_root_where_it_has_to_look_for_the_media_files)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
