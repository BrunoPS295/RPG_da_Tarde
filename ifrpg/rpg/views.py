from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import RPGmodel

# Create your views here.
@login_required
def rpg(request):
    rpgs = RPGmodel.objects.order_by('nome')
    context = {'rpgs': rpgs}
    return render(request, 'rpg/rpg.html', context)