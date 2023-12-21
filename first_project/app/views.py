from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os
from django.urls import reverse




def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время':  reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir_view'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def current_time(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime('%H:%M:%S')
    print (current_time)
    return HttpResponse(current_time)

def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    pages = {}
    for item in os.listdir(path='.'):
        pages[item] = reverse('workdir_view')
    context = {
        'pages': pages
    }
    return HttpResponse(str(pages))

