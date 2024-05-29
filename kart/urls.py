from django.urls import path
from kart import views


urlpatterns = [
    path('', views.home, name = 'home')
]