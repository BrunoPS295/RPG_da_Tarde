from django.shortcuts import render, get_object_or_404
from .models import Documentos
from .form import DocumentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect, FileResponse
from django.db.models import Q
import os
import mimetypes
# Create your views here.

@login_required
def documento(request):
    list = Documentos.objects.filter(
        Q(usuario=request.user) | Q(permitidos=request.user)
    ).distinct().order_by('-data')
    context = {'list': list}
    return render(request, 'documents/documento.html', context)

def acessar_documento(request, doc_id):
    documento = get_object_or_404(Documentos, id=doc_id)
    if not documento.arquivo:
        raise Http404("Arquivo não encontrado.")

    file_handle = documento.arquivo.open('rb')
    filename = os.path.basename(documento.arquivo.name)
    mime_type, _ = mimetypes.guess_type(filename)
    if not mime_type:
        mime_type = 'application/octet-stream'

    response = FileResponse(file_handle, content_type=mime_type)
    response['Content-Disposition'] = f'inline; filename="{filename}"'
    return response

def novo_documento(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            new_documento = form.save(commit=False)
            new_documento.usuario = request.user
            new_documento.save()
            form.save_m2m()
            list = Documentos.objects.order_by('data')
            context = {'list': list}
            return HttpResponseRedirect('/documentos/')
    else:
        form = DocumentForm(user=request.user)
    context = {'form': form}
    return render(request, 'documents/novo_documento.html', context)

def editar_documento(request, id):
    documentos = Documentos.objects.get(id=id)
    if documentos.usuario != request.user:
        raise Http404("Você não tem permissão para editar este documento.")
    else:
        if request.method == 'POST':
            if 'btn_deletar' in request.POST:
                documentos.delete()
                return HttpResponseRedirect('/documentos/')
            
            form = DocumentForm(request.POST, request.FILES, instance=documentos, user=request.user)
            if form.is_valid():
                list = Documentos.objects.order_by('data')
                form.save()
                context = {'list': list}
                return HttpResponseRedirect('/documentos/')
            
        else:
            form = DocumentForm(instance=documentos, user=request.user)
    document_id = documentos.id
    context = {'form': form, 'document_id': document_id}
    return render(request, 'documents/editar_documento.html', context)