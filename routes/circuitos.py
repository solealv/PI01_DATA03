from fastapi import APIRouter
from config.db import conn
from models.circuit import circuits
from schemas.circuit import Circuit

circuit = APIRouter()

@circuit.get('/circuit', response_model=list[Circuit])
def get_circuit():
    return conn.execute(circuits.select()).fetchall()
