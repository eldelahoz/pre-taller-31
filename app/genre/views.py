from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *


class GenderViewset(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
