from django.urls import path
from . import views
from .views import home, desktop

urlpatterns = [
    path('', views.terminal, name='terminal'),  # This maps the root URL to the terminal view
    path('desktop/', views.desktop, name='desktop'),
    path('terminal/', views.terminal, name='terminal'),
    path('snake/', views.snake, name='snake'),
    path('agenda/', views.agenda, name='agenda'),  # Added path for agenda
    path('desktop/create_tool/', views.create_tool, name='create_tool'),
    path('crypto/', views.crypto, name='crypto'),  # Added path for crypto
    path('explorer/', views.explorer, name='explorer'),  # Added path for explorer

]
