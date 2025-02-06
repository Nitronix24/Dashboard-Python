from django.shortcuts import render
from backend.APP.core.models import Icon  # Mise à jour de l'import

def homepage(request):
    icons = Icon.objects.all()
    return render(request, 'homepage.html', {'icons': icons})