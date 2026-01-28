from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('ola/<str:nome>/', views.saudacao, name='saudacao'),
]