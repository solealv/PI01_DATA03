from fastapi import APIRouter
from config.db import conn
from models.constructor import constructors

cons = APIRouter()

@cons.get('/constructor')
def get_constructor():
    return conn.execute(constructors.select()).fetchall()

