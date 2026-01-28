from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('contato/', views.contato, name='contato'),
    path('ola/<str:nome>/', views.saudacao, name='saudacao'),
]