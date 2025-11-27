from symbol import parameters

from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b= b

def home(request):
    data = {
        'title': 'Главная страница',
        'menu': [  # Переименовано в 'menu' для согласованности с шаблоном
            {'title': "Вход", 'url_name': 'login'},
            {'title': "Зарегистрироваться", 'url_name': 'register'}
        ],
        'float': 28.54,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 2, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},  # Исправлено: ключ: значение
        'obj': MyClass(10, 20),
    }
    return render(request, "main/home.html", context=data) # Обрабатывает шаблон и отправляет его клиенту

def about(request):
    return render(request, "main/about.html")

def login(request):
    return HttpResponse("Скоро тут можно будет войти")

def register(request):
    return HttpResponse("Скоро вы сможете зарегистрироваться")
# Функция обработки ошибок
#def page_not_found(request, exception):
  #  return redirect('notfound')

# Функция обработки шаблона ошибок
#def error(request):
  #  return render(request, "main/notfound.html")

def custom_404_view(request, exception):
    return render(request, 'main/404.html', status=404)