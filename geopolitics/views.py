from django.http import Http404
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def geopolitics(request):
    return render(request, "geopolitics.html")


def geopolitics_region(request, region):
    regions = {
        "north-america": {
            "name": "North America",
            "intro": (
                "Follow the decisions in the United States, Canada and Mexico "
                "that reshape trade, security and strategic industries."
            ),
            "dek": (
                "Y-SQRE tracks the policies and power shifts that move capital, "
                "reorder supply chains and create new constraints for business."
            ),
            "pillars": [
                {
                    "label": "Trade & Industry",
                    "title": "Supply chains, industrial policy and the future of regional trade",
                },
                {
                    "label": "Security & Alliances",
                    "title": "Defence priorities, the Arctic and North America's global role",
                },
                {
                    "label": "Technology & Capital",
                    "title": "Strategic technologies and the investment decisions behind them",
                },
                {
                    "label": "Policy Signals",
                    "title": "The domestic choices with consequences beyond national borders",
                },
            ],
            "sample_article": {
                "slug": "us-canada-relations-markets-crypto",
                "category": "Geopolitics & Markets",
                "title": "US-Canada relations: geopolitical shifts and their impact on stocks and cryptocurrencies",
                "dek": (
                    "Trade, energy security and strategic competition are reshaping "
                    "how investors assess opportunities across traditional markets and digital assets."
                ),
            },
        },
        "europe": {"name": "Europe"},
        "asia": {"name": "Asia"},
        "asean": {"name": "ASEAN"},
        "pacific": {"name": "Pacific"},
    }

    if region not in regions:
        raise Http404("Unknown geopolitics region")

    return render(
        request,
        "geopolitics_region.html",
        {"region": regions[region]},
    )


def geopolitics_article(request, region, slug):
    articles = {
        ("north-america", "us-canada-relations-markets-crypto"): {
            "region": "North America",
            "category": "Geopolitics & Markets",
            "title": "US-Canada relations: geopolitical shifts and their impact on stocks and cryptocurrencies",
            "dek": (
                "Trade, energy security and strategic competition are reshaping "
                "how investors assess opportunities across traditional markets and digital assets."
            ),
            "author": "Y-SQRE Research",
            "read_time": "7 min read",
        },
    }

    article = articles.get((region, slug))
    if article is None:
        raise Http404("Unknown geopolitics article")

    return render(request, "geopolitics_article.html", {"article": article})
