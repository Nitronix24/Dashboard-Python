from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ToolBox

def home (request):
    return render(request, 'apps/home.html')
def desktop(request):
    tools = ToolBox.objects.all()
    return render(request, "apps/desktop.html", {"tools": tools})

def create_tool(request):
    if request.method == "POST":
        name = request.POST.get("name")
        icon_url = request.POST.get("icon_url")
        color = request.POST.get("color", "#ffffff")
        url = request.POST.get("url")
        
        new_tool = ToolBox.objects.create(name=name, icon_url=icon_url, color=color, url=url)
        return JsonResponse({
            "id": new_tool.id,
            "name": new_tool.name,
            "icon_url": new_tool.icon_url,
            "color": new_tool.color,
            "url": new_tool.url
        })

    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_tool(request, tool_id):
    if request.method == "POST":
        tool = get_object_or_404(ToolBox, id=tool_id)
        tool.delete()
        return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"}, status=400)

def update_tool_size(request, tool_id):
    if request.method == "POST":
        tool = get_object_or_404(ToolBox, id=tool_id)
        tool.width = request.POST.get("width")
        tool.height = request.POST.get("height")
        tool.save()
        return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"}, status=400)


def terminal(request):
    return render(request, 'apps/terminal.html')
def agenda(request):
    return render(request, 'apps/agenda.html')
def snake(request):
    return render(request, 'apps/snake.html')
def crypto(request):
    return render(request, 'apps/crypto.html')
def explorer(request):
    return render(request, 'apps/file_explorer.html')