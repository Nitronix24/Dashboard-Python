from django.shortcuts import render
from django.http import JsonResponse
from .models import ToolBox

def home (request):
    return render(request, 'apps/home.html')

def terminal(request):
    return render(request, 'apps/terminal.html')
def desktop(request):
    tools = ToolBox.objects.all()
    return render(request, "apps/desktop.html", {"tools": tools})
def agenda(request):
    return render(request, 'apps/agenda.html')
def snake(request):
    return render(request, 'apps/snake.html')

def create_tool(request):
    if request.method == "POST":
        name = request.POST.get("name")
        icon_url = request.POST.get("icon_url")
        color = request.POST.get("color", "#ffffff")
        
        new_tool = ToolBox.objects.create(name=name, icon_url=icon_url, color=color)
        return JsonResponse({
            "id": new_tool.id,
            "name": new_tool.name,
            "icon_url": new_tool.icon_url,
            "color": new_tool.color
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


def crypto(request):
    return render(request, 'apps/crypto.html')

def explorer(request):
    return render(request, 'apps/file_explorer.html')