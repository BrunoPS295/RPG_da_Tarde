from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
import os
import mimetypes
from .forms import FichaForm
from .forms import gm_fichaForm
from .forms import AtaqueForm
from .forms import ItemForm
from .models import RPGmodel
from .models import Ficha
from .models import Itens

# Create your views here.
@login_required
def selecionar_fichas(request):
    rpg = RPGmodel.objects.filter(
        Q(mestre=request.user) | Q(jogadores=request.user)
    ).distinct()
    fichas = Ficha.objects.filter(
        Q(jogador=request.user, morte=False) | Q(rpg__mestre=request.user, morte=False)
    )
    context = {'fichas': fichas, 'rpg': rpg}
    return render(request, 'rpg/rpg.html', context)

def criar_ficha(request):
    rpgs = RPGmodel.objects.all()
    if request.method == 'POST':
        form = FichaForm(request.POST, user=request.user)
        if form.is_valid():
            new_ficha = form.save(commit=False)
            new_ficha.jogador = request.user
            new_ficha.save()
            return redirect('rpg', id=new_ficha.id)
    else:
        form = FichaForm(user=request.user)
    context = {'form': form, 'rpgs': rpgs}
    return render(request, 'rpg/ficha.html', context)

def rpg(request, id):
    ficha = get_object_or_404(Ficha, id=id)
    ataques = ficha.ataques_set.all().order_by('id')
    itens = ficha.itens_set.all().order_by('id')
    if ficha.morte:
        return render(request, 'rpg/morte.html')
    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha, user=request.user)
        form_ataque = AtaqueForm(request.POST)
        prof_checks = request.POST.getlist('prof_checks')
        
        if 'btn_excluir_ataque' in request.POST:
            ataque_id = request.POST.get('btn_excluir_ataque')
            ataque_to_delete = get_object_or_404(ficha.ataques_set, id=ataque_id)
            ataque_to_delete.delete()
            
        if 'btn_add_ataque' in request.POST:
            if form_ataque.is_valid():
                new_ataque = form_ataque.save(commit=False)
                new_ataque.ficha = ficha
                new_ataque.save()
                return redirect('rpg', id=ficha.id)
            else:
                print(form_ataque.errors)
                
        if 'btn_salvar_ficha' in request.POST:
            if form.is_valid():
                form.save()
                ficha.prof_check = prof_checks
                ficha.save()
                return redirect('rpg', id=ficha.id)
            else:
                print(form.errors)
    else:
        form = FichaForm(instance=ficha, user=request.user)
    context = {'form': form, 'ataques': ataques, 'ficha': ficha, 'itens': itens}
    return render(request, 'rpg/ficha.html', context)

def terminal(request):
    return render(request, 'rpg/terminal.html')

def painel_gm(request, id):
    rpg = get_object_or_404(RPGmodel, id=id)
    if request.user != rpg.mestre:
        return HttpResponse("Acesso negado: Você não é o mestre deste RPG.")
    
    ficha = None
    form = None

    

    if request.method == 'POST':
        ficha_id = request.POST.get('ficha_id')
        if not ficha_id:
            return HttpResponse("ID da ficha não fornecido.", status=400)
        ficha = get_object_or_404(Ficha, id=ficha_id, rpg=rpg, morte=False)
        form = gm_fichaForm(request.POST, instance=ficha, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('painel_gm', id=rpg.id)
        else:
            print(form.errors)

        

    context = {
        'rpg': rpg,
        'ficha': ficha,
        'fichas': Ficha.objects.filter(rpg=rpg, morte=False).order_by('id'),
        'itens': Itens.objects.filter(rpg_item=rpg).order_by('id'),
        'form': form,
    }
    return render(request, 'rpg/painel_gm.html', context)

#itens
def criar_item(request, id):
    rpg = get_object_or_404(RPGmodel, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.rpg_item = rpg
            new_item.save()
            return redirect('painel_gm', id=rpg.id)
    else:
        form = ItemForm()
    context = {'form': form, 'rpg': rpg}
    return render(request, 'rpg/criar_item.html', context)

def acessar_item(request, id):
    item = get_object_or_404(Itens, id=id)
    if not item.documento:
        raise Http404("Arquivo não encontrado.")
    file_handle = item.documento.open('rb')
    filename = os.path.basename(item.documento.name)
    mime_type, _ = mimetypes.guess_type(filename)
    if not mime_type:
        mime_type = 'application/octet-stream'

    response = FileResponse(file_handle, content_type=mime_type)
    response['Content-Disposition'] = f'inline; filename="{filename}"'
    return response

def editar_item(request, id):
    item = get_object_or_404(Itens, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if 'btn_deletar_item' in request.POST:
            item.delete()
            return redirect('painel_gm', id=item.rpg_item.id)
        if form.is_valid():
            form.save()
            return redirect('painel_gm', id=item.rpg_item.id)
       
        else:
            print(form.errors)
    else:
        form = ItemForm(instance=item)
    context = {'form': form, 'item': item}
    return render(request, 'rpg/editar_item.html', context)