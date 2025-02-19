from django.contrib import admin
from django.urls import path

from Pessoa import views as views_pessoa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoa/', views_pessoa.index, name='index-pessoa'),
    path('pessoa/add/', views_pessoa.cria, name='add-pessoa'),
    path('pessoa/edit/', views_pessoa.edita, name='edit-pessoa'),
    path('pessoa/delete/', views_pessoa.deleta, name='delete-pessoa'),
]
