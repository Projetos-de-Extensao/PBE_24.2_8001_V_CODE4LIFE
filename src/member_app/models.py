from django.db import models
from django.utils import timezone

class Convite(models.Model):
    CONVITE_TYPES_CHOICE = [
        ('PENDENTE', 'Pendente'),
        ('ENVIADO', 'Enviado'),        
    ]
    link = models.URLField()
    dataCriacao = models.DateTimeField(default=timezone.now)
    validade = models.DateTimeField()
    convite_type = models.CharField(max_length=10, choices=CONVITE_TYPES_CHOICE, default='PENDENTE')
    limiteConvites = models.IntegerField(default=1)

    def aceitar(self):
        """Aceita o convite, se ainda estiver válido."""
        if self.convite_type == "enviado" and timezone.now() <= self.validade:
            self.convite_type = "aceito"
            self.save()  
            return True
        else:
            print("Convite expirado ou já aceito.")
            return False

    def __str__(self):
        return (f"Convite(id={self.id}, link='{self.link}', dataCriacao={self.dataCriacao}, "
                f"validade={self.validade}, estado='{self.convite_type}', limiteConvites={self.limiteConvites})")
                
