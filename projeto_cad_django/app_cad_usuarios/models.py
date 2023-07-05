from django.db import models

# criando a tabela de usuarios
#para criar no terminal digite python .\manage.py makemigrations
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    cidade = models.TextField(max_length=255)
    email = models.TextField(max_length=255)


#para criar o banco de dados digite no terminal python .\manage.py migrate