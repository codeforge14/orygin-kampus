from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """Render the ORYGIN Kampus landing page."""
    context = {
        "page_title": "ORYGIN Kampus — Former aujourd'hui, inspirer demain",
        "meta_description": (
            "ORYGIN Kampus accompagne les talents de Guyane vers leur épanouissement "
            "professionnel à travers des programmes innovants d'insertion, de formation "
            "et d'accompagnement personnalisé."
        ),
    }
    return render(request, "home.html", context)
