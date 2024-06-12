from django.urls import path
from . import views

urlpatterns = [
    path('footgram/', views.footgram, name='footgram'),
]