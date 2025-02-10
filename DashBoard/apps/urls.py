from django.urls import path
from . import views
from .views import home, desktop , create_tool , delete_tool

urlpatterns = [
    path('home/', views.home, name='home'),
    path('desktop/', views.desktop, name='desktop'),
    path('desktop/create_tool/', views.create_tool, name='create_tool'), 
    path('desktop/delete_tool/<int:tool_id>/', views.delete_tool, name='delete_tool'),
]
