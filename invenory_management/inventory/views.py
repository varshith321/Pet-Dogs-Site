from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

def index(request):
    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'about.html')

def meetpups(request):
    return render(request, 'meet_pups.html')

def menu(request):
    return render(request, 'menu.html')

def reservations(request):
    return render(request, 'reservations.html')
    
def contact(request):
    return render(request, 'contact.html')


def display_pup(request):
    items = Pup.objects.all()
    context = {
        'items': items,
        'header': 'Pup',
    }
    return render(request, 'meet_pups.html', context)