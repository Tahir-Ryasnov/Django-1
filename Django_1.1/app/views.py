import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    return render(request, 'app/time.html', context={'current_time': current_time})


def workdir_view(request):
    workdir = os.listdir(path='.')
    return render(request, 'app/workdir.html', context={'workdir': workdir})
