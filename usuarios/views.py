from django.shortcuts import render
from usuarios.forms import loginForm, CadastroForm


def login(request):
    form = loginForm()
    return render(request, 'usuarios/login.html', {"form" : form} )

def cadastro(request):
    form = CadastroForm()
    return render(request, 'usuarios/cadastro.html',{"form" : form} )