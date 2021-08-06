from django.urls import path
from .views import aposta_view, regra_view

urlpatterns = [
    path('apostalist/', aposta_view.ApostaList.as_view(), name='aposta-list'),
    path('apostadetails/<int:id>', aposta_view.ApostaDetails.as_view() , name='aposta-details'),

    path('apostacamplist/', aposta_view.ApostaCamp.as_view(), name='apostacamp-list'), 

    path('regralist/', regra_view.RegraList.as_view(), name='regra-list'),
    path('regradetails/<int:id>', regra_view.RegraDetails.as_view() , name='regra-details'), 
]