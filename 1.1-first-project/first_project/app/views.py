from django.http import HttpResponse
from django.shortcuts import render, reverse

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'главная страница': reverse('home'),
        'показать текущее время': reverse('time'),
        'показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    import datetime
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    msg = f'текущее время: {current_time}'
    
    return HttpResponse(msg)

def workdir_view(request):
    import os
    files = os.listdir('.')
    files_str = ', '.join(files)
    return HttpResponse(f'Содержимое рабочей директории: {files_str}')