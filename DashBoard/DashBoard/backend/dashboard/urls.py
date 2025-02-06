from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('APP.core.urls')),       # updated include
    path('api/desktop/', include('APP.dekstop.urls')),   # updated include to match folder name
]
