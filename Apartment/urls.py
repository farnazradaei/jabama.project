from django.urls import path
from .views import Book_Apartment
urlpatterns = [
    path('hello/' , Book_Apartment ) ,
]