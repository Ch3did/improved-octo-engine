from django.contrib import admin
from OMDb_API.models import Livros

class Livro(admin.ModelAdmin):
    list_display = ('id','titulo','isbn','autor','editora','edição','numero_de_pgs','descrição')
    list_display_links = ('id',)
    search_fields = ('title', 'isbn','autor','editora')
    list_per_page = 20

admin.site.register(Livros, Livro)


