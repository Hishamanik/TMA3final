from django.shortcuts import render

def index(request):
    return render(request, 'tma3c.html')