from django.urls import path
from .views import apostajogo_view

urlpatterns = [
    path('apostalist/', apostajogo_view.ApostaJogoList.as_view(), name='aposta-list'),
    path('apostadetails/<int:id>', apostajogo_view.ApostaJogoDetails.as_view() , name='aposta-details'),

    path('apostacamplist/', apostajogo_view.ApostaJogoCamp.as_view(), name='apostacamp-list'),  
]