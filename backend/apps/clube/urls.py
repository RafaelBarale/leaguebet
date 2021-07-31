from django.urls import path
from .views import clube_view

urlpatterns = [
    path('list/', clube_view.ClubeList.as_view(), name='clube-list'),
    path('details/<int:id>', clube_view.ClubeDetails.as_view() , name='clube-details'),
]