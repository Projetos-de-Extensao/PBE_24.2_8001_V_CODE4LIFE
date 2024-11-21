from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from .models import Convite
from .serializers import ConviteSerializer

class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Convite.objects.all()
    serializer_class = ConviteSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        """Associa o convite ao usuário logado."""
        serializer.save(usuario=self.request.user)

    @action(detail=True, methods=['post'])
    def aumentar(self, request, pk=None):
        try:
            convite = self.get_object()
            convite.aumentar_convites()
            serializer = self.get_serializer(convite)
            return Response(serializer.data)
        except Convite.DoesNotExist:
            return Response({"detail": "Convite não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def enviar(self, request, pk=None):
        convite = self.get_object()
        assunto = "Convite para Participar"
        mensagem = convite.mensagem or f"Você foi convidado! Acesse o link: {convite.link}"
        destinatario = [convite.email]

        try:
            send_mail(assunto, mensagem, 'seuemail@dominio.com', destinatario)
            convite.convite_type = 'ENVIADO'
            convite.save()
            return Response({"status": "Email enviado com sucesso!"})
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)