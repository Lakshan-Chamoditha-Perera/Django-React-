from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def main (request):
    return  HttpResponse('Hello',status=200)


def test (request):
    return  HttpResponse('Test',status=200)