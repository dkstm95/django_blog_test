from django.shortcuts import render

from .models import Pictures

# Create your views here.

def home(request):
    pictures = Pictures.objects
    return render(request, 'home.html', {'blogs': pictures})
