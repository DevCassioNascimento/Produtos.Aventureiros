from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProdutoForm
from .models import Produto
from django.contrib.auth.decorators import login_required
from django.urls import reverse



@login_required
def painel_view(request):
    return render(request, 'painel.html')

def redirecionar_para_login(request):
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect(reverse('painel'))  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmasenha = request.POST['confirmasenha']

        if senha != confirmasenha:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Esse nome de usuário já existe.')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
        return redirect('login')
    return render(request, 'cadastro.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Cadastro de produtos

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            return redirect('produtos')  
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

def lista_produtos(request):
    produtos = Produto.objects.all().order_by('-data_criacao')
    return render(request, 'lista_produtos.html', {'produtos': produtos})



