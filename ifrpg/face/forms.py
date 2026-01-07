from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=150, required=True)
    fields = ['username']
    labels = {
        'username': 'Nome de Usuário',
        }