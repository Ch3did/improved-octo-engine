from rest_framework import viewsets
from OMDb_API.models import Livros 
from OMDb_API.serializer import LivrosSerializer

class LivrosViewset(viewsets.ModelViewSet):
    """Crud de Livros"""
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer