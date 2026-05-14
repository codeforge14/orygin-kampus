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


def mission(request: HttpRequest) -> HttpResponse:
    """Render the mission & valeurs page."""
    context = {
        "page_title": "Notre mission — ORYGIN Kampus",
        "meta_description": (
            "Découvrez la mission, les valeurs et l'histoire d'ORYGIN Kampus, "
            "organisme de formation et d'insertion professionnelle en Guyane française."
        ),
        "milestones": _MILESTONES,
    }
    return render(request, "mission.html", context)


def parcours(request: HttpRequest) -> HttpResponse:
    """Render the parcours page."""
    context = {
        "page_title": "Nos parcours — ORYGIN Kampus",
        "meta_description": (
            "Un accompagnement en 4 leviers : orientation, formation, insertion et suivi "
            "post-emploi. Découvrez la méthode ORYGIN Kampus pour votre projet professionnel."
        ),
    }
    return render(request, "parcours.html", context)


def offres(request: HttpRequest) -> HttpResponse:
    """Render the offres de formation page."""
    context = {
        "page_title": "Nos offres de formation — ORYGIN Kampus",
        "meta_description": (
            "Accompagnement à l'emploi, Français Langue Étrangère et formations supérieures. "
            "Financement CPF, OPCO, France Travail disponible. Certifié Qualiopi."
        ),
    }
    return render(request, "offres.html", context)


def partenaires(request: HttpRequest) -> HttpResponse:
    """Render the partenaires page."""
    context = {
        "page_title": "Nos partenaires — ORYGIN Kampus",
        "meta_description": (
            "ORYGIN Kampus s'appuie sur un réseau de partenaires institutionnels, "
            "d'entreprises et d'universités pour accompagner les talents de Guyane."
        ),
    }
    return render(request, "partenaires.html", context)


def qui_sommes_nous(request: HttpRequest) -> HttpResponse:
    """Render the qui sommes-nous page."""
    context = {
        "page_title": "Qui sommes-nous — ORYGIN Kampus",
        "meta_description": (
            "ORYGIN Kampus est une SCOP guyanaise engagée dans la formation et l'insertion "
            "professionnelle depuis 2012. Découvrez notre identité, notre gouvernance et notre équipe."
        ),
    }
    return render(request, "qui_sommes_nous.html", context)


def contact(request: HttpRequest) -> HttpResponse:
    """Render the contact page."""
    context = {
        "page_title": "Nous contacter — ORYGIN Kampus",
        "meta_description": (
            "Contactez ORYGIN Kampus à Cayenne, Mana ou Kourou. "
            "Entretien gratuit, réponse sous 48h."
        ),
    }
    return render(request, "contact.html", context)
