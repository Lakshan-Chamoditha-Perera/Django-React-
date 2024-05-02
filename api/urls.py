from django.urls import path
from .views import RoomView, main,test

urlpatterns = [
    path('hello/', main),
    path('test/', test),
    path('home', RoomView.as_view())  
]
