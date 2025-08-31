
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from content.sitemaps import sitemaps
from vectorsite import settings
from django.contrib.sitemaps.views import sitemap

"""Обработка ошибок"""

handler403 = 'content.views.tr_handler403'
handler404 = 'content.views.tr_handler404'
handler500 = 'content.views.tr_handler500'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('content.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
