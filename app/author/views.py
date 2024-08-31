from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer