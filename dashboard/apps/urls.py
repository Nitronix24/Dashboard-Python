from django.urls import path
from . import views
from .views import home, desktop, create_tool, delete_tool, update_tool, terminal, agenda, snake, crypto, explorer

urlpatterns = [
    path('', views.home, name='home'),  
    path('home/', views.home, name='home'),
    path('desktop/', views.desktop, name='desktop'),
    path('desktop/create_tool/', views.create_tool, name='create_tool'),
    path('desktop/delete_tool/<int:tool_id>/', views.delete_tool, name='delete_tool'),
    path('desktop/update_tool/<int:tool_id>/', views.update_tool, name='update_tool'),

    #Addes path for tools
    path('terminal/', views.terminal, name='terminal'),
    path('snake/', views.snake, name='snake'),
    path('agenda/', views.agenda, name='agenda'),  
    path('crypto/', views.crypto, name='crypto'), 
    path('explorer/', views.explorer, name='explorer'),
    path('navigateur/', views.navigateur, name='navigateur'),
    path('meteo/', views.meteo, name='meteo'),
    path('chat/', views.chat, name='chat'),
]
