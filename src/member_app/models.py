from django.db import models
from django.utils import timezone

class Convite(models.Model):
    link = models.URLField()
    dataCriacao = models.DateTimeField(default=timezone.now)
    validade = models.DateTimeField()
    estado = models.CharField(max_length=50, default="enviado")
    limiteConvites = models.IntegerField(default=1)

    def aceitar(self):
        """Aceita o convite, se ainda estiver válido."""
        if self.estado == "enviado" and timezone.now() <= self.validade:
            self.estado = "aceito"
            self.save()  
            return True
        else:
            print("Convite expirado ou já aceito.")
            return False

    def __str__(self):
        return (f"Convite(id={self.id}, link='{self.link}', dataCriacao={self.dataCriacao}, "
                f"validade={self.validade}, estado='{self.estado}', limiteConvites={self.limiteConvites})")
