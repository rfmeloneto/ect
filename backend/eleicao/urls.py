
from django.urls import path

from .views import CandidatoListView, UrnaAPI

urlpatterns = [
    path('api/salvar_urna/', UrnaAPI.as_view(), name='salvar_urna'),
    path('api/listar_votos/', CandidatoListView.as_view(), name='listar_urna'),
]
