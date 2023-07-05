from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('',views.home,name='home'),
    path('usuarios/', views.usuarios,name='listagem_de_usuarios'),    
    path('usuarios/excluir/<int:id_usuario>/', views.excluir_usuario, name='excluir_usuario'),
]

