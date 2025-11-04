from django.urls import path
from .views import hello,bye,edad


urlpatterns = [
    path('hello', hello),
    path('bye', bye),
    path('edad/<int:anios>/<int:futuro>', edad)
]
