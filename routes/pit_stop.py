from fastapi import APIRouter
from config.db import conn
from models.pit_stop import pit_stops

pit_stop = APIRouter()

@pit_stop.get('/pit_stop')
def get_pit_stop():
    return conn.execute(pit_stops.select()).fetchall()

