from django.urls import path
from sensorizador import views

app_name = 'sensorizador'

urlpatterns = [
    path('<int:id>/', views.pesquisa, name='pesquisa'),
    path('sensorizador/registrar/', views.create, name='registrar'),
    path('sensorizador/analisar/', views.analise, name='analise'),
    path('sensorizador/enviacsv/', views.enviacsv, name='enviacsv'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
