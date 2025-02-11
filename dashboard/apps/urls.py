from django.urls import path
from . import views
from .views import home, desktop, create_tool, terminal, agenda, snake, crypto, explorer

urlpatterns = [
    path('', views.home, name='home'),  
    path('home/', views.home, name='home'),
    path('desktop/', views.desktop, name='desktop'),
    path('desktop/create_tool/', views.create_tool, name='create_tool'),

    #Addes path for tools
    path('terminal/', views.terminal, name='terminal'),
    path('snake/', views.snake, name='snake'),
    path('agenda/', views.agenda, name='agenda'),  
    path('crypto/', views.crypto, name='crypto'), 
    path('explorer/', views.explorer, name='explorer'),
]
