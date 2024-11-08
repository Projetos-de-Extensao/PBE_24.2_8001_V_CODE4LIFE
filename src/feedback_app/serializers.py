from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['usuario', 'texto', 'feedback_type', 'dataHoraEnvio']