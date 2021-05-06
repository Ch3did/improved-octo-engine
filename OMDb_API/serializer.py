from rest_framework import serializers
from OMDb_API.models import Livros



class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = ['id', 'titulo','isbn','autor','editora','edição','numero_de_pgs','descrição']
    