from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('salom hammaga')


def about(request):
    return HttpResponse('Salom about')


def asd(request):
    return HttpResponse('Salom asd')


# http://127.0.0.1:8000/Nasriddin
def Nasriddin(request):
    return HttpResponse('Assalomu alaykum Nasriddin')

# http://127.0.0.1:8000/Muhammadali


def Muhammadali(request):
    return HttpResponse('Assalomu alaykum Muhammadali')

# http://127.0.0.1:8000/Muhammad


# http://127.0.0.1:8000/Nasriddin
def Abdushukur(request):
    return HttpResponse('Assalomu alaykum Abdushukur brother')

# http://127.0.0.1:8000/Samandar

def Samandar(request):
    return HttpResponse('Assalomu alaykum Samandar')

# http://127.0.0.1:8000/Abdurashid

def Abdurashid(request):
    return HttpResponse('Assalomu alaykum Abdurashid')


def Muhammad(request):
    return HttpResponse('Assalomu alaykum Muhammad')

# http://127.0.0.1:8000/Mukaddam/


def Mukaddam(request):
    return HttpResponse('Assalomu alaykum Mukaddam sister')

# http://127.0.0.1:8000/Mohinur


def Mokhinur(request):
    return HttpResponse('Assalomu alaykum Mohinur sister')

# http://127.0.0.1:8000/Maftuna


def Maftuna(request):
    return HttpResponse('Assalomu alaykum Maftuna sister')
