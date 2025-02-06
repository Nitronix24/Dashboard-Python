from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),       # URLs pour l'application core
    path('api/desktop/', include('desktop.urls')), # URLs pour l'application desktop
]
