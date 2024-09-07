from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description

# Initialize FastAPI
app = FastAPI()

# Define your data model for Product
class Order(BaseModel):
    product: str
    units: int
    
class Product(BaseModel):
    name: str
    notes: str

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}
  
@app.get("/hello")
async def hello_endpoint(name: str = 'World'):
    return {"message": f"Hello, {name}!"}