from django.shortcuts import render

def deskpage(request):
    return render(request, 'deskpage.html')