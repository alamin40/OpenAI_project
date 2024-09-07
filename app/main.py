from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description

# Initialize FastAPI
app = FastAPI()

# Define your data model for Product
class Order(BaseModel):
    product: str
    units: int
    
