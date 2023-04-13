# from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from fastapi import FastAPI
from configs.db_config import db_connection_keep_on
from models.userModel import User
import json

from app.routes.auth

app = FastAPI()

db = db_connection_keep_on()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# router = APIRouter()
@app.get("/get_all_employees")
def get_all_users():
    users = json.loads(User.objects().to_json())

    return {"users": users}

@app.get("/")
def read_root():
    return {
        "Hello": "World"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
