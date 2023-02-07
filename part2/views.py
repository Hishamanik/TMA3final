from django.shortcuts import render

def index(request):
    return render(request, 'part2/index.html')