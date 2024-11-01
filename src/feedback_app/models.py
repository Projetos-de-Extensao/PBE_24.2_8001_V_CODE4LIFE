from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  

class Feedback(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produtoId = models.IntegerField() 
    texto = models.TextField()
    tipo = models.CharField(max_length=50)
    dataHoraEnvio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f"Feedback(id={self.id}, usuarioId={self.usuario.id}, produtoId={self.produtoId}, "
                f"texto='{self.texto}', tipo='{self.tipo}', dataHoraEnvio={self.dataHoraEnvio})")

