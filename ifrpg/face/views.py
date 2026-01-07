from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, get_user_model, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import Login
from .forms import LoginForm
# Create your views here.

@login_required
def index(request):
    return render(request, 'face/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username', '').strip().lower()
            user, created = User.objects.get_or_create(username=username)

            if created:
                user.set_password('123456@abc')
                user.save()

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, user)
            return redirect('index')
          
    else:
        form = LoginForm()
        
    context = {'form': form}
    return render(request, 'face/login.html', context)
            

def logout_view(request):
    logout(request)
    return render(request, 'face/login.html')
