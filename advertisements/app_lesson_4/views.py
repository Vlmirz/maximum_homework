from django.shortcuts import render
from django.http import HttpResponse


def homework(request):
    return HttpResponse('Домашка по 4 занятию')