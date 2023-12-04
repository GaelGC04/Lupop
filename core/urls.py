from django.urls import path
from .views import home, usuario_info

urlpatterns = [
    path('', home, name='home'),
    path('usuario_info/', usuario_info, name='usuario_info'),
]