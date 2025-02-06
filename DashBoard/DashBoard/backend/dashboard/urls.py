from django.contrib import admin
from django.urls import path, include
from frontend.pages.deskpage import deskpage
from frontend.pages.homepage import homepage 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('api/core/', include('APP.core.urls')),
    path('api/desktop/', include('APP.dekstop.urls')),
]
