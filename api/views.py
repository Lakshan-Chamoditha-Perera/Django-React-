from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer

# Create your views here.


def main (request):
    return  HttpResponse('Hello',status=200)


def test (request):
    return  HttpResponse('Test',status=200)

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer