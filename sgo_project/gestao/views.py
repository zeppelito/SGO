from django.shortcuts import render, redirect
from .models import NotificacaoAcidente
from .forms import NotificacaoAcidenteForm

def criar_notificacao(request):
    if request.method == 'POST':
        form = NotificacaoAcidenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = NotificacaoAcidenteForm()
    
    return render(request, 'criar_notificacao.html', {'form': form})
