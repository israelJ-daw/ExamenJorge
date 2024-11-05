from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path("ultimo/voto<int:vendido_id>/", views.ultimo_voto, name="ultimo_voto")
]
