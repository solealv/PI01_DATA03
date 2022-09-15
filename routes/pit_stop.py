from fastapi import APIRouter
from config.db import conn
from models.pit_stop import pit_stops
from schemas.pit_stop import Pit_stop

pit_stop = APIRouter()

@pit_stop.get('/pit_stop', response_model=list[Pit_stop])
def get_pit_stop():
    return conn.execute(pit_stops.select()).fetchall()

