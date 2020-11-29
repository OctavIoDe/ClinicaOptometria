# Django
from django.shortcuts import render

def HomeView(peticion):
    ctx = {
        'titulo': 'Inicio'
    }
    return render(peticion, 'clinica/index.html', ctx)