from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Convite
from .serializers import ConviteSerializer

class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Convite.objects.all()
    serializer_class = ConviteSerializer

    @action(detail=True, methods=['post'])
    def aumentar(self, request, pk=None):
        try:
            convite = self.get_object()  
            convite.aumentar_convites()
            serializer = self.get_serializer(convite)
            return Response(serializer.data)

        except Convite.DoesNotExist:
            return Response({"detail": "Convite não encontrado."}, status=status.HTTP_404_NOT_FOUND)




