from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirecionar_para_login, name='home'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('painel/', views.painel_view, name='painel'),
    path('produtos/', views.lista_produtos, name='produtos'),



]
