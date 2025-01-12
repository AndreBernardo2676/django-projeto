from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html ', context={
        'nome': 'André Luiz',
    })


def contato(request):
    return render(request, 'recipes/contato.html') 


def sobre(request):
    return HttpResponse('sobre')
