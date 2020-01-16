import logging
from django.shortcuts import render
from django.views.generic import TemplateView

from land.models import Subscribtion
from land.forms import SubscribeForm


logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'land/index.html')


def handler500(request):
    return render(request, "land/500.html")


class PageView(TemplateView):
    pass


def subscribe(request):

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscribe = Subscribtion(email=form.cleaned_data['email'])
            subscribe.save()
            return render(request, 'lessons/thankyou.html')
    else:
        form = SubscribeForm()

    return render(
        request,
        'land/subscribe.html',
        {'form': form}
    )
