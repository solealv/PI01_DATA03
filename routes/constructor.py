from fastapi import APIRouter
from config.db import conn
from models.constructor import constructors
from schemas.constructor import Constructor

cons = APIRouter()

@cons.get('/constructor', response_model=list[Constructor])
def get_constructor():
    return conn.execute(constructors.select()).fetchall()

