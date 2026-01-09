from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import RPGmodel

# Create your views here.
@login_required
def selecionar_rpg(request):
    rpgs = RPGmodel.objects.order_by('nome')
    context = {'rpgs': rpgs}
    return render(request, 'rpg/rpg.html', context)

def rpg(request, id):
    rpgs = RPGmodel.objects.get(id=id)
    context = {'rpgs': rpgs}
    return render(request, 'rpg/ficha.html', context)