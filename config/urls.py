from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import handler500
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('', include('land.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'land.views.handler500'
