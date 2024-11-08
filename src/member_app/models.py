from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Convite(models.Model):
    CONVITE_TYPES_CHOICE = [
        ('PENDENTE', 'Pendente'),
        ('ENVIADO', 'Enviado'),
        ('ACEITO', 'Aceito'),
    ]
    link = models.URLField()
    dataCriacao = models.DateTimeField(default=timezone.now)
    validade = models.DateTimeField()
    convite_type = models.CharField(max_length=10, choices=CONVITE_TYPES_CHOICE, default='PENDENTE')
    limiteConvites = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)])

    def aumentar_convites(self):
       
        if self.limiteConvites < 1:
            self.limiteConvites = 1
        
        elif self.limiteConvites < 10:
            self.limiteConvites += 1
        else:
            print("Limite máximo de convites atingido.")
        self.save() 

    def aceitar(self):
        if self.convite_type == "ENVIADO" and timezone.now() <= self.validade:
            self.convite_type = "ACEITO"
            self.save()
            return True
        else:
            print("Convite expirado ou já aceito.")
            return False

    def __str__(self):
        return (f"Convite(id={self.id}, link='{self.link}', dataCriacao={self.dataCriacao}, "
                f"validade={self.validade}, estado='{self.convite_type}', limiteConvites={self.limiteConvites})")



                
