from django.urls import path
from .views import main,test

urlpatterns = [
    path('hello/', main),
    path('test/', test)
    
]
