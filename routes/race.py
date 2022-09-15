from fastapi import APIRouter
from config.db import conn
from models.race import races
from schemas.race import Race

race = APIRouter()

@race.get('/race', response_model=list[Race])
def get_race():
    return conn.execute(races.select()).fetchall()

