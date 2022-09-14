from fastapi import APIRouter
from config.db import conn
from models.race import races

race = APIRouter()

@race.get('/race')
def get_race():
    return conn.execute(races.select()).fetchall()

