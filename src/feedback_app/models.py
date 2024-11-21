from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Feedback(models.Model):
    FEEDBACK_TYPES_CHOICE = [
        ('----------', '----------'),
        ('RECLAME', 'Reclamação'),
        ('SUGESTA', 'Sugestão'),
        ('ELOGIO', 'Elogio'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    texto = models.TextField()
    feedback_type = models.CharField(max_length=10, choices=FEEDBACK_TYPES_CHOICE, default='----------')
    dataHoraEnvio = models.DateTimeField(default=timezone.now) 

    def _str_(self):
        return f"Feedback(id={self.id}, usuarioId={self.usuario.id}, texto='{self.texto}', tipo='{self.feedback_type}', dataHoraEnvio={self.dataHoraEnvio})"

