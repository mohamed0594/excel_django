from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def accueil(request):
    return HttpResponse(" ne soyez pas amoureux de ma premiere realisation")


def contact(request):
    return HttpResponse( "ceci est ma toute premiere realisation de ma  page contact")

def blog(request):
    return HttpResponse (" vous aimez monnn blog......")

