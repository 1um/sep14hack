import json
from textwrap import dedent
from typing import Dict

from openai import AsyncOpenAI

from actions.domain import Action
from keys import openai_api_key

client = AsyncOpenAI(api_key=openai_api_key)


async def generate_suggested_query_params(user_query: str, action: Action) -> Dict:
    prompt = dedent(f"""
        Given the user query: "{user_query}"

        And the following action metadata:
        - ID: {action.id}
        - Name: {action.metadata.teaser.header}
        - Description: {action.metadata.teaser.description}
        - Query Parameters Schema: {action.metadata.query_params_schema}
        - Default Query Parameters: {action.metadata.default_query_params}

        Generate suggested query parameters that would be effective for using this specific action.
        The suggestions should be relevant to the user's query and comply with the given schemas.

        Do not repeat the default query parameters, if you want to keep them.
        Do not make up new query parameters.
        Add only parameters you want to change into the suggested query parameters.

        Provide your response in the JSON format. Don't use Markdown.
    """)

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates suggested parameters for API actions based on user queries.",
            },
            {"role": "user", "content": prompt},
        ],
        response_format={
            "type": "json_object",
        },
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )

    suggested_params = response.choices[0].message.content.strip()

    # Parse the JSON string into a Python dictionary
    try:
        suggested_query_params = json.loads(suggested_params)
    except json.JSONDecodeError:
        # If parsing fails, return an empty dictionary
        suggested_query_params = {}

    # Remove suggested params that are the same as default params
    default_params = action.metadata.default_query_params or {}
    suggested_query_params = {
        k: v
        for k, v in suggested_query_params.items()
        if k not in default_params or v != default_params[k]
    }

    print("suggested_query_params", suggested_query_params)

    return suggested_query_params
