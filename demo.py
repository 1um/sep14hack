from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def demo(request: Request):
    return templates.TemplateResponse("demo.html", {"request": request})
