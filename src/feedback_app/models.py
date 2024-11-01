from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  

class Feedback(models.Model):
    FEEDBACK_TYPES_CHOICE = [
        ('RECLAME', 'Reclamação'),
        ('SUGESTA', 'Sugestão'),
        ('ELOGIO', 'Elogio'),        
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    feedback_type = models.CharField(max_length=10, choices=FEEDBACK_TYPES_CHOICE, default='RECLAME')
    dataHoraEnvio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f"Feedback(id={self.id}, usuarioId={self.usuario.id}, produtoId={self.produtoId}, "
                f"texto='{self.texto}', tipo='{self.tipo}', dataHoraEnvio={self.dataHoraEnvio})")

