from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ['usuario']  # Torna o campo 'usuario' somente leitura
    fields = ['usuario', 'texto', 'feedback_type', 'dataHoraEnvio']  # Campos exibidos no formulário

    def save_model(self, request, obj, form, change):
        """Define automaticamente o usuário logado ao salvar."""
        if not change or not obj.usuario:  # Preenche apenas se for novo ou não definido
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        """Garante que o campo 'usuario' seja somente leitura para edições."""
        if obj:  # Durante a edição, torna o campo apenas leitura
            return self.readonly_fields + ['usuario']
        return self.readonly_fields

admin.site.register(Feedback, FeedbackAdmin)