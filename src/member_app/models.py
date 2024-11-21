from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Convite(models.Model):
    CONVITE_TYPES_CHOICE = [
        ('PENDENTE', 'Pendente'),
        ('ENVIADO', 'Enviado'),
        ('ACEITO', 'Aceito'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    link = models.URLField()
    dataCriacao = models.DateTimeField(default=timezone.now)
    validade = models.DateTimeField(null=True, blank=True)
    convite_type = models.CharField(max_length=10, choices=CONVITE_TYPES_CHOICE, default='PENDENTE')
    limiteConvites = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    mensagem = models.TextField(blank=True, null=True)

    def aumentar_convites(self):
        if self.limiteConvites < 10:
            self.limiteConvites += 1
        self.save()

    def aceitar(self):
        if self.convite_type == "ENVIADO" and timezone.now() <= self.validade:
            self.convite_type = "ACEITO"
            self.save()
            return True
        return False
    def _str_(self):
        return f"Convite(id={self.id}, email='{self.email}', link='{self.link}', estado='{self.convite_type}')"
                
