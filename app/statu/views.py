from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()