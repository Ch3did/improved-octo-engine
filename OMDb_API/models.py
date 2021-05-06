from django.db import models


class Livros(models.Model):
    titulo = models.CharField(max_length=70,blank=False)
    isbn = models.IntegerField (blank=False)
    autor = models.CharField(max_length=70, blank=False)
    editora = models.CharField(max_length=70, blank=False)
    edição = models.IntegerField(blank=False)
    numero_de_pgs = models.IntegerField(blank=False)
    descrição = models.TextField(max_length=300) 
