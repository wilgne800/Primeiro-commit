from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        cidade = request.POST.get('cidade')
        email = request.POST.get('email')

        if nome:  # Verifica se o campo nome foi preenchido
            novo_usuario = Usuario(nome=nome, idade=idade, cidade=cidade, email=email)
            novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def excluir_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.delete()
    return redirect('listagem_de_usuarios')
