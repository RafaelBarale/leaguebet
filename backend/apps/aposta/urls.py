from django.urls import path
from .views import aposta_view

urlpatterns = [
    path('apostalist/', aposta_view.ApostaList.as_view(), name='aposta-list'),
    path('apostadetails/<int:id>', aposta_view.ApostaDetails.as_view() , name='aposta-details'),

    path('apostacamplist/', aposta_view.ApostaCamp.as_view(), name='apostacamp-list'),  
]