import random
from string import ascii_uppercase, ascii_lowercase, punctuation, digits

from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length', 10))
    characters = list(ascii_lowercase)
    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list(punctuation))
    if request.GET.get('numbers'):
        characters.extend(list(digits))
    the_password = ''
    for i in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def the_about(request):
    return render(request, 'generator/about.html', {'about': the_about})
