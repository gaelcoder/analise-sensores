from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sensores', views.SensorViewSet, basename='sensor')

app_name = 'sensorizador'

urlpatterns = [
    path('api/', include(router.urls)),
    path('<int:id>/', views.pesquisa, name='pesquisa'),
    path('sensorizador/registrar/', views.create, name='registrar'),
    path('sensorizador/analisar/', views.analise, name='analise'),
    path('sensorizador/enviacsv/', views.enviacsv, name='enviacsv'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]

