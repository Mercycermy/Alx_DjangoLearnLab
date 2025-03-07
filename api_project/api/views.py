from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
