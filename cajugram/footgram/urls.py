from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registration/', views.signup_view, name='registration'),
    path('user-home/', views.user_home, name='user_home'),
]