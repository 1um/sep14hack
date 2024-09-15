from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, HttpUrl


class Teaser(BaseModel):
    header: str
    subheader: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[HttpUrl] = None
    images: Optional[List[HttpUrl]] = None


class ActionMetadata(BaseModel):
    id: str
    teaser: Teaser
    url: HttpUrl
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
    headers: Optional[Dict[str, str]] = None
    query_params_schema: Optional[Dict] = None
    body_schema: Optional[Dict] = None
    suggested_query_params: Optional[Dict] = None


class Action(BaseModel):
    id: str
    metadata: ActionMetadata
    match_score: float
    cost_per_action: float
