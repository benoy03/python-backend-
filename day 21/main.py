from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Dummy in-memory database
items_db = [
    {"id": 1, "name": "Item One", "description": "First item"},
    {"id": 2, "name": "Item Two", "description": "Second item"},
]

posts_db = [
    {"id": 1, "user_id": 1, "title": "First Post", "status": "published"},
    {"id": 2, "user_id": 1, "title": "Draft Post", "status": "draft"},
    {"id": 3, "user_id": 2, "title": "Another Post", "status": "published"},
]

class Item(BaseModel):
    name: str
    description: Optional[str] = None

@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, World!"})

@app.get("/greet/{name}", response_class=HTMLResponse)
async def greet(request: Request, name: str):
    return templates.TemplateResponse("greet.html", {"request": request, "name": name})

# -------------------- Items Endpoints --------------------
@app.get("/items/{item_id}", response_class=HTMLResponse)
async def get_item(request: Request, item_id: int, name: Optional[str] = None):
    filtered_items = [item for item in items_db if item["id"] == item_id]
    if name:
        filtered_items = [item for item in filtered_items if name.lower() in item["name"].lower()]
    if not filtered_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return templates.TemplateResponse("items.html", {"request": request, "items": filtered_items})

@app.post("/items", response_class=HTMLResponse)
async def create_item(request: Request, item: Item):
    new_id = max([i["id"] for i in items_db]) + 1 if items_db else 1
    new_item = {"id": new_id, "name": item.name, "description": item.description}
    items_db.append(new_item)
    return templates.TemplateResponse("create_item.html", {"request": request, "item": new_item})

# -------------------- User Posts Endpoint --------------------
@app.get("/users/{user_id}/posts", response_class=HTMLResponse)
async def get_user_posts(request: Request, user_id: int, status: Optional[str] = Query(None)):
    user_posts = [post for post in posts_db if post["user_id"] == user_id]
    if status:
        user_posts = [post for post in user_posts if post["status"] == status]
    return templates.TemplateResponse("user_posts.html", {"request": request, "posts": user_posts, "user_id": user_id, "status": status})
