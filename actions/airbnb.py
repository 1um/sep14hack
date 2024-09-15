from pydantic import HttpUrl

from actions.domain import ActionMetadata, Teaser
from keys import x_rapidapi_key

airbnb_search_action = ActionMetadata(
    id="airbnb_search",
    teaser=Teaser(
        header="Search Airbnb Listings",
        subheader="Millions of active listings from real hosts",
        logo=HttpUrl(
            "https://a0.muscache.com/airbnb/static/logos/belo-200x200-4d851c5b28f61931bf1df28dd15e60ef.png"
        ),
        images=[
            HttpUrl(
                "https://a0.muscache.com/im/pictures/06fb8c2c-30de-41c4-b882-a703007e02e3.jpg?ml=true&im_w=960"
            ),
            HttpUrl(
                "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6NTQ4ODUwOQ%3D%3D/original/1abf9fd3-4e9c-4166-ac54-d52ec164eda6.jpeg?im_w=1200"
            ),
            HttpUrl(
                "https://a0.muscache.com/im/pictures/miso/Hosting-1044162865400976036/original/6429ba9b-1c55-47a9-99c6-4272e238f581.jpeg?im_w=1200"
            ),
            HttpUrl(
                "https://a0.muscache.com/im/pictures/miso/Hosting-744724115822075381/original/a298f731-b778-4249-9d67-2b25ac4cebc8.jpeg?im_w=1200"
            ),
            HttpUrl(
                "https://a0.muscache.com/im/pictures/prohost-api/Hosting-1001232776784508975/original/ebb614fa-c544-4ed8-a254-0af4255906e3.jpeg?im_w=1200"
            ),
        ],
    ),
    url=HttpUrl("https://airbnb19.p.rapidapi.com/api/v1/searchPropertyV2"),
    method="GET",
    headers={
        "x-rapidapi-key": x_rapidapi_key,
        "x-rapidapi-host": "airbnb19.p.rapidapi.com",
    },
    query_params_schema={
        "type": "object",
        "properties": {
            "category": {"type": "string", "default": "TAB_8225"},
            "totalRecords": {"type": "integer", "default": 10},
            "currency": {"type": "string", "default": "USD"},
            "adults": {"type": "integer", "default": 1},
            "children": {"type": "integer", "default": 0},
            "infants": {"type": "integer", "default": 0},
            "pets": {"type": "integer", "default": 0},
            "checkin": {"type": "string", "format": "date"},
            "checkout": {"type": "string", "format": "date"},
        },
        "required": ["checkin", "checkout"],
    },
    suggested_query_params={
        "arrival_date": "2024-09-25",
        "departure_date": "2024-10-02",
    },
)
