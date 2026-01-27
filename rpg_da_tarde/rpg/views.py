from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import FichaForm
from .models import RPGmodel
from .models import Ficha

# Create your views here.
@login_required
def selecionar_fichas(request):
    fichas = Ficha.objects.filter(
        Q(jogador=request.user) | Q(rpg__mestre=request.user)
    )
    context = {'fichas': fichas}
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
    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha, user=request.user)
        prof_checks = request.POST.getlist('prof_checks')
        if form.is_valid():
            form.save()
            ficha.prof_check = prof_checks
            ficha.save()
            return redirect('rpg', id=ficha.id)
    else:
        form = FichaForm(instance=ficha, user=request.user)
    context = {'form': form, 'ficha': ficha}
    return render(request, 'rpg/ficha.html', context)

def terminal(request):
    return render(request, 'rpg/terminal.html')