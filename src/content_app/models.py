from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    autenticado = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  

    def autenticar(self, senha):
        """Verifica se a senha está correta para autenticar o usuário."""
        if self.senha == senha:
            self.autenticado = True
            self.save()  
            return True
        else:
            self.autenticado = False
            self.save()
            return False

    def __str__(self):
        return f"Usuário(id={self.id}, nome='{self.nome}', email='{self.email}', autenticado={self.autenticado})"

class Content(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo





    
    
