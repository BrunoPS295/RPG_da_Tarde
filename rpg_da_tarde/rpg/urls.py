from django.urls import path
from . import views

urlpatterns = [
    path("", views.selecionar_rpg, name='selecionar_rpg'),
    path("<int:id>/", views.rpg, name='rpg'),
]