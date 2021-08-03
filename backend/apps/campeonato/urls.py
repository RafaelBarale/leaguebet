from django.urls import path
from .views import campeonato_view, classificacao_view, jogo_view, rodada_view

urlpatterns = [
    path('camplist/', campeonato_view.CampeonatoList.as_view(), name='campeonato-list'),
    path('campdetails/<int:id>', campeonato_view.CampeonatoDetails.as_view() , name='campeonato-details'),

    path('classlist/', classificacao_view.ClassificacaoList.as_view(), name='classificacao-list'),
    path('classdetails/<int:id>', classificacao_view.ClassificacaoDetails.as_view() , name='classificacao-details'),
    path('classcamplist/', classificacao_view.ClassifCamp.as_view(), name='classcamp-list'),  
    
    path('rodadalist/', rodada_view.RodadaList.as_view(), name='rodada-list'),
    path('rodadadetails/<int:id>', rodada_view.RodadaDetails.as_view() , name='rodada-details'),
    path('rodadacamplist/', rodada_view.RodadaCamp.as_view() , name='rodadacamp-list'),
    
    path('jogolist/', jogo_view.JogoList.as_view(), name='jogo-list'),
    path('jogodetails/<int:id>', jogo_view.JogoDetails.as_view() , name='jogo-details'),
    path('jogosrodadacamplist/', jogo_view.JogoRodadaCamp.as_view() , name='jogosrodadacamp-list'),       
    
]