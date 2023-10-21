from typing import List
from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

# Define your Recipe class
class Recipe(BaseModel):
    id: int
    title: str
    instructions: str
        
# Create database
DB: List[Recipe] = [
    Recipe(id=1, title="Panda Express Chicken Terriyaki", instructions="Add"),
    Recipe(id=2, title="Spicy Thai Basil Chicken", instructions="Add"),
    Recipe(id=3, title="Thai Red Curry with Chicken", instructions="Add"),
    Recipe(id=4, title="Healthy Salmon Bowl", instructions="Add"),
    Recipe(id=5, title="Instant Pot Chicken Tortilla Soup", instructions="Add"),
    
]

# Change your path to api and return database
@app.get("/api")
def read_root():
    return DB
