from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Categoria(models.TextChoices):
    AVENTUREIROS = 'Aventureiros', 'Aventureiros'
    DESBRAVADORES = 'Desbravadores', 'Desbravadores'

class TipoNegocio(models.TextChoices):
    VENDA = 'Venda', 'Venda'
    TROCA = 'Troca', 'Troca'

class Produto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=Categoria.choices)
    tipo_negocio = models.CharField(max_length=10, choices=TipoNegocio.choices)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nome
    
    # Cadastro de produtos 
    



