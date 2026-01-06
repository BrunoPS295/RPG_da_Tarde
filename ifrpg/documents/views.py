from django.shortcuts import render
from .models import Documentos
from .form import DocumentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def documento(request):
    list = Documentos.objects.order_by('data')
    context = {'list': list}
    return render(request, 'documents/documento.html', context)

def novo_documento(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            list = Documentos.objects.order_by('data')
            context = {'list': list}
            return render(request, 'documents/documento.html', context)
    else:
        form = DocumentForm(request.POST)
    context = {'form': form}
    return render(request, 'documents/novo_documento.html', context)

def editar_documento(request, id):
    documentos = Documentos.objects.get(id=id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=documentos)
        if form.is_valid():
            form.save()
            list = Documentos.objects.order_by('data')
            context = {'list': list}
            return render(request, 'documents/documento.html', context)
    else:
        form = DocumentForm(instance=documentos)
    document_id = documentos.id
    context = {'form': form, 'document_id': document_id}
    return render(request, 'documents/editar_documento.html', context)