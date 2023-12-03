from django.urls import path
from munecos import views

urlpatterns = [
    path('', views.presentacion),
]