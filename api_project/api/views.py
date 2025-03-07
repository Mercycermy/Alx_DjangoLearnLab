from django.shortcuts import render
from  .serializers import Bookserializer
from .models import Book
from rest_framework import generics

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
