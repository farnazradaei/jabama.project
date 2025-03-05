from django.urls import path
from .views import book_cottage
urlpatterns = [
    path('hello/' , book_cottage ) ,
]