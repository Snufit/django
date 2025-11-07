from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.
def index(request): # HttpRequest
    return HTTPResponse("Страница приложения PF_DPP.")