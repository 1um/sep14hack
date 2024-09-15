import os

from fastapi import HTTPException

# Load OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise HTTPException(
        status_code=500, detail="OpenAI API key not found in environment variables"
    )

x_rapidapi_key = os.getenv("X_RAPIDAPI_KEY")
if not x_rapidapi_key:
    raise HTTPException(
        status_code=500, detail="X-RapidAPI key not found in environment variables"
    )
