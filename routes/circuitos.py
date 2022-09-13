from fastapi import APIRouter
from config.db import conn
from models.tables import circuits

circuit = APIRouter()

@circuit.get('/circuit')
def get_circuit():
    return conn.execute(circuits.select()).fetchall()
