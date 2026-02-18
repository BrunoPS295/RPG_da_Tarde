from django.urls import path
from . import views

urlpatterns = [
    path("", views.selecionar_fichas, name='selecionar_fichas'),
    path("ficha/", views.criar_ficha, name='criar_ficha'),
    path("ficha/<int:id>/", views.rpg, name='rpg'),
    path("painel_gm/<int:id>/", views.painel_gm, name='painel_gm'),
    path("terminal/", views.terminal, name='terminal'),
    path("criar_item/<int:id>/", views.criar_item, name='criar_item'),
    path("acessar_item/<int:id>/", views.acessar_item, name='acessar_item'),
    path("editar_item/<int:id>/", views.editar_item, name='editar_item'),
]