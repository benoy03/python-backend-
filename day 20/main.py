from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, World!"})


@app.get("/greet/{name}", response_class=HTMLResponse)
async def greet(request: Request, name: str):
    return templates.TemplateResponse("greet.html", {"request": request, "name": name})
