from typing import List, Optional

from fastapi import FastAPI, HTTPException
from llama_index.embeddings.openai import OpenAIEmbedding
from pydantic import BaseModel
from retrieval.vector_store import ActionVectorStore

from actions.airbnb import airbnb_search_action
from actions.booking import booking_search_action
from actions.domain import Action
from actions.linkedin import linkedin_search_action_metadata  # Add this line
from actions.social_search import social_search_action_metadata  # Add this line
from keys import openai_api_key

app = FastAPI()

# Initialize the vector store and embed model
embed_model = OpenAIEmbedding(api_key=openai_api_key)
vector_store = ActionVectorStore()

# Define actions to be added
action_metadatas = {
    airbnb_search_action.id: airbnb_search_action,
    booking_search_action.id: booking_search_action,
    linkedin_search_action_metadata.id: linkedin_search_action_metadata,
    social_search_action_metadata.id: social_search_action_metadata,
}

# Add actions to the vector store
vector_store.add_actions(action_metadatas, embed_model)


class QueryParams(BaseModel):
    user_context_embedding: Optional[List[float]] = None
    user_context_text: Optional[str] = None
    session_id: Optional[str] = None
    user_id: Optional[str] = None


@app.post("/", response_model=List[Action])
async def query_actions(params: QueryParams) -> List[Action]:
    # Prepare the query embedding
    if params.user_context_embedding:
        query_embedding = params.user_context_embedding
    elif params.user_context_text:
        query_embedding = embed_model.get_query_embedding(params.user_context_text)
    else:
        raise HTTPException(
            status_code=400,
            detail="Either user_context_embedding or user_context_text must be provided",
        )

    # Query the vector store
    query_result = vector_store.query(query_embedding, top_k=2)

    # Prepare the actions list
    retrieved_actions = [
        Action(
            id=id,
            metadata=vector_store.get_action_metadata(id),
            match_score=score,
            cost_per_action=0.001,
        )
        for id, score in zip(query_result.ids, query_result.similarities)
    ]

    return retrieved_actions
