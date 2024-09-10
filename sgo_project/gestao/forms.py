from django import forms
from .models import NotificacaoAcidente

class NotificacaoAcidenteForm(forms.ModelForm):
    class Meta:
        model = NotificacaoAcidente
        fields = '__all__'
