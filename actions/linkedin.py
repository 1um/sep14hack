from typing import Any, Dict

from pydantic import BaseModel

from actions.domain import ActionMetadata, Teaser


class LinkedInSearchParams(BaseModel):
    keywords: str
    start: str = "0"
    geo: str = ""
    company: str = ""


def linkedin_search_action(params: LinkedInSearchParams) -> Dict[str, Any]:
    import requests

    url = "https://linkedin-data-api.p.rapidapi.com/search-people"

    querystring = {
        "keywords": params.keywords,
        "start": params.start,
        "geo": params.geo,
        "company": params.company,
    }

    headers = {
        "x-rapidapi-key": "8619b9205amsh1b57064c1ec8fdcp174354jsnbbe3c4383a1a",
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


linkedin_search_action_metadata = ActionMetadata(
    id="linkedin_search",
    name="LinkedIn Search",
    description="Search for people on LinkedIn based on keywords, location, and company",
    method="GET",
    url="https://linkedin-data-api.p.rapidapi.com/search-people",
    headers={
        "x-rapidapi-key": "8619b9205amsh1b57064c1ec8fdcp174354jsnbbe3c4383a1a",
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
    },
    suggested_query_params={
        "keywords": "max",
        "start": "0",
        "geo": "103644278,101165590",
        "company": "Pinterest",
    },
    teaser=Teaser(
        header="LinkedIn People Search",
        subheader="Find professionals on LinkedIn",
        description="Search for people on LinkedIn based on keywords, location, and company",
        logo="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg",
    ),
)
