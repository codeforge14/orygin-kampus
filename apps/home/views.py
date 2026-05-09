from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

_MILESTONES: list[dict[str, str]] = [
    {
        "year": "2012",
        "title": "Fondation d'ORYGIN",
        "desc": "Création de la structure initiale avec un premier service d'accompagnement socio-professionnel à Cayenne.",
    },
    {
        "year": "2015",
        "title": "Statut SCOP",
        "desc": "Transformation en Société Coopérative et Participative. Les salariés deviennent acteurs de la gouvernance.",
    },
    {
        "year": "2017",
        "title": "Ouverture FLE & Interculturel",
        "desc": "Lancement des formations Français Langue Étrangère et des ateliers interculturels pour les primo-arrivants.",
    },
    {
        "year": "2019",
        "title": "Agence Digitale",
        "desc": "Création de l'entité numérique pour répondre aux besoins de transformation digitale des entreprises guyanaises.",
    },
    {
        "year": "2021",
        "title": "Parcours Entreprise",
        "desc": "Déploiement du programme d'accompagnement à la création et au développement d'entreprise.",
    },
    {
        "year": "2023",
        "title": "Programmes Masters",
        "desc": "Partenariats universitaires signés pour proposer des formations de niveau Master en Guyane.",
    },
    {
        "year": "2026",
        "title": "ORYGIN Kampus",
        "desc": "Réunion des 6 entités sous le label ORYGIN Kampus pour une offre intégrée et cohérente sur le territoire.",
    },
]


def home(request: HttpRequest) -> HttpResponse:
    """Render the ORYGIN Kampus landing page."""
    context = {
        "page_title": "ORYGIN Kampus — Former aujourd'hui, inspirer demain",
        "meta_description": (
            "ORYGIN Kampus accompagne les talents de Guyane vers leur épanouissement "
            "professionnel à travers des programmes innovants d'insertion, de formation "
            "et d'accompagnement personnalisé."
        ),
        "milestones": _MILESTONES,
    }
    return render(request, "home.html", context)
