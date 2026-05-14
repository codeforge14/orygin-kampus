from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("mission/", views.mission, name="mission"),
    path("parcours/", views.parcours, name="parcours"),
    path("offres/", views.offres, name="offres"),
    path("partenaires/", views.partenaires, name="partenaires"),
    path("qui-sommes-nous/", views.qui_sommes_nous, name="qui_sommes_nous"),
    path("contact/", views.contact, name="contact"),
]
