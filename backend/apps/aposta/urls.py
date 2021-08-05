from django.urls import path
from .views import aposta_view, pontuacao_view

urlpatterns = [
    path('apostalist/', aposta_view.ApostaList.as_view(), name='aposta-list'),
    path('apostadetails/<int:id>', aposta_view.ApostaDetails.as_view() , name='aposta-details'),

    path('apostacamplist/', aposta_view.ApostaCamp.as_view(), name='apostacamp-list'), 

    path('pontuacaolist/', pontuacao_view.PontuacaoList.as_view(), name='pontuacao-list'),
    path('pontuacaodetails/<int:id>', pontuacao_view.PontuacaoDetails.as_view() , name='pontuacao-details'), 
]