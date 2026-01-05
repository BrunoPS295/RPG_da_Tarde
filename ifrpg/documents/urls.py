from django.urls import path
from . import views

urlpatterns = [
    path('', views.documento, name='documento'),
    path('novo/', views.novo_documento, name='novo_documento'),
    path('editar/<int:id>/', views.editar_documento, name='editar_documento'),
]
