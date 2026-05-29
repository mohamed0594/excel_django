from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def accueil(request):
    context = {
        "nom":"mohamed",
        "age":24,
        "prenom": "amine",
        "est_connecte":True,
        "couleurs":["noir", "orange", "red","green", "fucha", "white", "black"]
    }
    return render(request, 'accueil.html', context)


def contact(request):
    context = {
        "mon numero":5767686876,
        "email":"doumbiamohamedaime.gmail.com",
        "copyright":"gdgdhjdg"

    }
    return  render(request,'contact.html', context)

def blog(request):
    context = {
        "papa":"pagne",
        "maman":"robe"
    }
    return render(request, 'blog.html', context)

