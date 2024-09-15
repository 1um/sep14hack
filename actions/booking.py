from pydantic import HttpUrl

from actions.domain import ActionMetadata, Teaser
from keys import x_rapidapi_key

booking_search_action = ActionMetadata(
    id="booking_search",
    teaser=Teaser(
        header="Search Booking.com Hotels",
        subheader="Find and book accommodations worldwide",
        logo=HttpUrl("https://cdn.worldvectorlogo.com/logos/bookingcom-1.svg"),
        images=[
            HttpUrl(
                "https://cf.bstatic.com/xdata/images/hotel/max1280x900/134044726.jpg?k=959c3a6fd4030b335ac4f590ef676b99afa982853fc55eea1e0b33218af29fc7&o=&hp=1"
            ),
            HttpUrl(
                "https://cf.bstatic.com/xdata/images/hotel/max1280x900/304789516.jpg?k=d635cf2bb0b7e1d6bfc30d7270cd99ff6b5674cb92ea63aadfd3d5173417522d&o=&hp=1"
            ),
            HttpUrl(
                "https://cf.bstatic.com/xdata/images/hotel/max1280x900/221358162.jpg?k=14def6754fcdf61da14d11c862bcb95c97813a5f3944469a642e6854bc784bd1&o=&hp=1"
            ),
            HttpUrl(
                "https://cf.bstatic.com/xdata/images/hotel/max1280x900/441149622.jpg?k=00be51d4c41ab052fc293f6da76e792a68ef4e68f54ee9cb0f2a97da23d368ad&o=&hp=1"
            ),
            HttpUrl(
                "https://cf.bstatic.com/xdata/images/hotel/max1280x900/484864079.jpg?k=069022999d27904402386fb32ace5e78829f2f03c35ebc6ba8317e34959cc755&o=&hp=1"
            ),
        ],
    ),
    url=HttpUrl(
        "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotelsByCoordinates"
    ),
    method="GET",
    headers={
        "x-rapidapi-key": x_rapidapi_key,
        "x-rapidapi-host": "booking-com15.p.rapidapi.com",
    },
    query_params_schema={
        "type": "object",
        "properties": {
            "latitude": {"type": "string"},
            "longitude": {"type": "string"},
            "arrival_date": {"type": "string", "format": "date"},
            "departure_date": {"type": "string", "format": "date"},
            "adults": {"type": "string", "default": "1"},
            "children_age": {"type": "string", "default": "0,17"},
            "room_qty": {"type": "string", "default": "1"},
            "units": {"type": "string", "default": "metric"},
            "page_number": {"type": "string", "default": "1"},
            "temperature_unit": {"type": "string", "default": "c"},
            "languagecode": {"type": "string", "default": "en-us"},
            "currency_code": {"type": "string", "default": "EUR"},
        },
        "required": ["latitude", "longitude", "arrival_date", "departure_date"],
    },
    default_query_params={
        "latitude": "19.24232736426361",
        "longitude": "72.85841985686734",
        "arrival_date": "2024-09-25",
        "departure_date": "2024-10-02",
        "room_qty": "1",
        "adults": "1",
        "children_age": "0,0",
        "units": "imperial",
        "page_number": "1",
        "temperature_unit": "f",
        "languagecode": "en-us",
        "currency_code": "USD",
    },
)
