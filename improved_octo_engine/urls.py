from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from OMDb_API.views import LivrosViewset

router = routers.DefaultRouter()
router.register('livros', LivrosViewset , basename='Livros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
