from django.urls import path
from . import views
from .views import home, desktop

urlpatterns = [
    path('home/', views.home, name='home'),
    path('desktop/', views.desktop, name='desktop'),
    path('desktop/create_tool/', views.create_tool, name='create_tool') 
]
