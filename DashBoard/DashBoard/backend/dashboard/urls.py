from django.contrib import admin
from django.urls import path, include
from frontend.pages.deskpage import deskpage 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', deskpage, name='home'),
    path('api/core/', include('APP.core.urls')),
    path('api/desktop/', include('APP.dekstop.urls')),
]
