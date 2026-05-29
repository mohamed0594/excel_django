from . import views
from django.urls import path
urlpatterns = [
    path("",views.accueil, name="accueil"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name= "blog")
]