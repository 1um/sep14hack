from textwrap import dedent

import openai

from actions.domain import ActionMetadata
from keys import openai_api_key

openai.api_key = openai_api_key


def generate_action_query(user_query: str, action: ActionMetadata) -> str:
    prompt = dedent(f"""
        Given the user query: "{user_query}"

        And the following schema:
        {action.query_params_schema}

        And the following suggested query:
        {action.suggested_query}

        Generate a new suggested query that would be more effective for given user query.

        Suggested query:""")

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates improved search queries.",
            },
            {"role": "user", "content": prompt},
        ],
        output_format={"type": "json_object"},
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    breakpoint()
    return response.choices[0].message["content"].strip()
