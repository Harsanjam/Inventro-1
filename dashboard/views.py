from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def inventory(request):
    return render(request, "inventory.html")

def login(request):
    return render(request, "login.html")

