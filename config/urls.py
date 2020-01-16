from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler500

urlpatterns = [
    path('', include('land.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

handler500 = 'land.views.handler500'
