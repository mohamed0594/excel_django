from . import views
from django.urls import path
urlpatterns = [
    path("",views.accueil),
    path("contact/", views.contact),
    path("blog/", views.blog)
]