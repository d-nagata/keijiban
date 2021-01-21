from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def top(request):
    return render(request, 'ban/top.html')