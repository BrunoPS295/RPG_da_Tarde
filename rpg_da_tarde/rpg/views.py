from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import FichaForm
from .forms import gm_fichaForm
from .forms import AtaqueForm
from .models import RPGmodel
from .models import Ficha

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
            
        if form.is_valid():
            form.save()
            ficha.prof_check = prof_checks
            ficha.save()
            return redirect('rpg', id=ficha.id)
        else:
            print(form.errors)
        if form_ataque.is_valid():
            form_ataque.save()
            return redirect('rpg', id=ficha.id)
        else:
            print(form_ataque.errors)
    else:
        form = FichaForm(instance=ficha, user=request.user)
    context = {'form': form, 'ataques': ataques, 'ficha': ficha}
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
        'fichas': Ficha.objects.filter(rpg=rpg).order_by('id'),
        'form': form,
    }
    return render(request, 'rpg/painel_gm.html', context)