from django.urls import path
from .views import criar_notificacao

urlpatterns = [
    path('criar_notificacao/', criar_notificacao, name='criar_notificacao'),
]
