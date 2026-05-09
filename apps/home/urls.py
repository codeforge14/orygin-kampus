from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("mission/", views.mission, name="mission"),
    path("parcours/", views.parcours, name="parcours"),
    path("offres/", views.offres, name="offres"),
    path("partenaires/", views.partenaires, name="partenaires"),
    path("contact/", views.contact, name="contact"),
]
