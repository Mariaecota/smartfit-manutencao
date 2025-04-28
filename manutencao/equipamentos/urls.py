from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_equipamentos, name='lista_equipamentos'),
    path('editar/<int:pk>/', views.editar_equipamento, name='editar_equipamento'),
]
