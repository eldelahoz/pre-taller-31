from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *


class BookViewset(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

