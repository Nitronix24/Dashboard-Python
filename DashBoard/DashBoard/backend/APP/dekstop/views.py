from rest_framework import generics, permissions
from .models import Application, Desktop
from .serializers import ApplicationSerializer, DesktopSerializer

class ApplicationListCreateView(generics.ListCreateAPIView):
    """Lister toutes les applications disponibles ou en ajouter une nouvelle."""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

class DesktopRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """Récupérer ou modifier le bureau d'un utilisateur."""
    queryset = Desktop.objects.all()
    serializer_class = DesktopSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Desktop.objects.filter(user=self.request.user)