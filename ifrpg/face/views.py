from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login as auth_login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Login
# Create your views here.

@login_required
def index(request):
    return render(request, 'face/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        if not username:
            return render(request, 'face/login.html', {'error': 'Digite um nome'})
        User = get_user_model()
        user, created = User.objects.get_or_create(username=username)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)
        Login.objects.get_or_create(player_nome=user.username)
        return render(request, 'face/index.html')
    return render(request, 'face/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'face/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            authenticate_user = authenticate(username = form.cleaned_data.get('username'), password= request.POST['password1'])
            return render(request, 'face/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'face/signup.html', {'form': form})