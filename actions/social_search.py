from typing import Any, Dict

from pydantic import BaseModel

from actions.domain import ActionMetadata, Teaser


class SocialSearchParams(BaseModel):
    query: str
    social_networks: str = (
        "facebook,tiktok,instagram,snapchat,twitter,youtube,linkedin,github,pinterest"
    )


def social_search_action(params: SocialSearchParams) -> Dict[str, Any]:
    import requests

    url = "https://social-links-search.p.rapidapi.com/search-social-links"

    querystring = {"query": params.query, "social_networks": params.social_networks}

    headers = {
        "x-rapidapi-key": "8619b9205amsh1b57064c1ec8fdcp174354jsnbbe3c4383a1a",
        "x-rapidapi-host": "social-links-search.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


social_search_action_metadata = ActionMetadata(
    id="social_search",
    method="GET",
    url="https://social-links-search.p.rapidapi.com/search-social-links",
    headers={
        "x-rapidapi-key": "8619b9205amsh1b57064c1ec8fdcp174354jsnbbe3c4383a1a",
        "x-rapidapi-host": "social-links-search.p.rapidapi.com",
    },
    default_query_params={
        "query": "John Smith",
        "social_networks": "facebook,tiktok,instagram,snapchat,twitter,youtube,linkedin,github,pinterest",
    },
    teaser=Teaser(
        header="Social Media Search",
        subheader="Search for social media profiles across multiple platforms by name. Who is John Smith on TikTok?",
        description="Search for social media profiles on Facebook, TikTok, Instagram, Snapchat, Twitter, YouTube, LinkedIn, GitHub, and Pinterest",
        logo="https://cdn-icons-png.flaticon.com/512/2065/2065157.png",
    ),
)
