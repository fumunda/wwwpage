from django.urls import path

from land import views
from land.views import PageView

app_name = 'land'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'subscribe',
        views.subscribe,
        name='subscribe'
    ),
    path('500', views.handler500, name='handler500')
]

pages = [
    'privacy',
    'imprint',
    'about',
    'cookies',
]

for page in pages:
    urlpatterns.append(
        path(
            page,
            PageView.as_view(template_name=f"land/{page}.html"),
            name=page
        ),
    )
