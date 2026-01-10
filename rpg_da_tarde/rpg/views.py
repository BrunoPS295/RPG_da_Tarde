from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import RPGmodel
from .models import Ficha

# Create your views here.
@login_required
def selecionar_rpg(request):
    rpgs = RPGmodel.objects.order_by('nome')
    context = {'rpgs': rpgs}
    return render(request, 'rpg/rpg.html', context)

def rpg(request, id):
    rpgs = RPGmodel.objects.get(id=id)
    fichas = Ficha.objects.filter(rpg_nome=rpgs, jogador=request.user or request.user == rpgs.mestre)
    if request.user == rpgs.mestre:
        context = {'rpgs': rpgs, 'fichas': fichas}
        return render(request, 'rpg/painel_gm.html', context)
    else:
        context = {'rpgs': rpgs, 'fichas': fichas}
        return render(request, 'rpg/ficha.html', context)