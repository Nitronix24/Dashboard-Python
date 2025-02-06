from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to my Django site!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/core/', include('APP.core.urls')),
    path('api/desktop/', include('APP.dekstop.urls')),
]
