from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'), # http://127.0.0.1:8000/main/
    path("about/", views.about, name='about'),
    path("login/", views.login, name = 'login'),
    path("register/", views.register, name = 'register'),
#    path("notfound/", views.error, name='notfound'), # Представление ошибки
]