from django.urls import path
from .views import login_view, exit, registro

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login_view'),
    path('exit/', exit, name='exit'),
]