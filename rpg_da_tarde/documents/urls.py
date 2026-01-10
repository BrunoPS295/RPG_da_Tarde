from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.documento, name='documento'),
    path('novo/', views.novo_documento, name='novo_documento'),
    path('editar/<int:id>/', views.editar_documento, name='editar_documento'),
    path('documento/ver/<int:doc_id>/', views.acessar_documento, name='abrir_documento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

