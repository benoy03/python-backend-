# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Minimal FastAPI API")

# Enable CORS for all origins (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to frontend URL if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

# Example API endpoint
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "description": f"This is item {item_id}"}
    print("sal")