from django.urls import path
from . import views

urlpatterns = [
    path("", views.selecionar_fichas, name='selecionar_fichas'),
    path("ficha/", views.criar_ficha, name='criar_ficha'),
    path("ficha/<int:id>/", views.rpg, name='rpg'),
    path("painel_gm/<int:id>/", views.painel_gm, name='painel_gm'),
    path("terminal/", views.terminal, name='terminal')
]