from django.urls import path 
from .views import Book_Apartment
urlpatterns = [
    path('Apartment/hello/' , Book_Apartment ) ,
   
]
