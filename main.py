from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from demo import app as demo_app
from query import app as query_app

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(url="/demo")


# Include the routes from index.py under the "/demo" path
app.mount("/demo", demo_app)  # Changed from "/index" to "/demo"

# Include the routes from query.py under the "/query" path
app.mount("/query", query_app)
