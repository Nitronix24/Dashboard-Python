from django.urls import path
from .views import ApplicationListCreateView, DesktopRetrieveUpdateView

urlpatterns = [
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('desktop/', DesktopRetrieveUpdateView.as_view(), name='desktop-detail'),
]