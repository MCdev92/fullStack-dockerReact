from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

### this application will have cors enable to automatically defend the application
# against "cross origin request" because the react application is a completely different application 
# than the FastAPI application. Therefore, corse need to be enable. ###

app = FastAPI()

# CORS added
origins = [
       "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define your Recipe class
class RecipeBase(BaseModel):
       title = str
       ingredients = str
       directions = str

class RecipeModel(RecipeBase):
    id: int
    
    class Config:
        orm_mode = True

# Database dependencies.
# get_db (dependencies injection), try create a db connection or close the db 
# make sure connection string opens when request comes in and close when request complete
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

# first enpoint for recipes application
# based on everything on recipe base, all variables are mapped from recipe base to table recipe into sqlite db
@app.post("/recipes/", response_model=RecipeModel)
async def create_recipe(recipe: RecipeBase, db: db_dependency):
    db_recipe = models.Transaction(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

# Get API endpoint
# query parameter to allow us to fetch a certain amount of recipes
@app.get("/recipes/", response_model = List[RecipeModel])
async def read_recipes(db: db_dependency, skip: int = 0, limit: int = 100):
    recipes = db.query(models.recipes).offset(skip).limit(limit).all()
    return recipes

