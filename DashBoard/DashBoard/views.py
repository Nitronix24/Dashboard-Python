from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from apps.models import Account
import bcrypt

def login (request):
    return render(request, 'login.html')

def create(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        profile_photo = request.FILES.get("profile_photo")

        if Account.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        account = Account(username=username, password=hashed_password.decode('utf-8'), profile_photo=profile_photo)
        account.save()

        redirect('login')

    return render(request, 'create.html')


def check (request) :
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            account = Account.objects.get(username=username)
        except Account.DoesNotExist:
            return JsonResponse({"error": "Invalid username or password"}, status=400)

        if bcrypt.checkpw(password.encode('utf-8'), account.password.encode('utf-8')):
            return JsonResponse({"success": "Login successful", "redirect_url": "/apps/desktop/"})
        else:
            return JsonResponse({"error": "Invalid username or password"}, status=400)