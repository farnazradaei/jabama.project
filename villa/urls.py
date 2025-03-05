from django.urls import path
from .views import book_villa
urlpatterns = [
    path('villa/hello/' , book_villa ) ,
]