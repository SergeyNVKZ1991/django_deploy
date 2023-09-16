import datetime
from os import listdir

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    date = datetime.datetime.now().time()
    # current_time = date.strftime('%H:%M')
    msg = f'Текущее время: {date}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    path = request.GET.get("path", r'F:\1. Обучение\4. Нетология\Конспекты\Django\Home_work_1\dj-homeworks')
    files = [f for f in listdir(path)]
    msg = f'Файлы рабочей директории: {files}'
    return HttpResponse(msg)
