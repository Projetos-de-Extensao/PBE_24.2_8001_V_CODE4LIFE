from django.utils.html import format_html
from django.contrib import admin
from .models import Convite

class ConviteAdmin(admin.ModelAdmin):
    readonly_fields = ['usuario']  # Campo 'usuario' como apenas leitura
    fields = ['usuario', 'email', 'link', 'dataCriacao', 'validade', 'convite_type', 'limiteConvites', 'mensagem']

    def save_model(self, request, obj, form, change):
        """Define automaticamente o usuário logado ao salvar."""
        if not change or not obj.usuario:
            obj.usuario = request.user  # Define o usuário logado
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        """Bloqueia a edição do campo 'usuario'."""
        if obj:  # Torna o campo 'usuario' somente leitura ao editar
            return self.readonly_fields + ['usuario']
        return self.readonly_fields

admin.site.register(Convite, ConviteAdmin)