from fastapi import APIRouter
from config.db import conn
from models.driver import drivers
from schemas.driver import Driver

driver = APIRouter()

@driver.get('/driver', response_model=list[Driver])
def get_driver():
    return conn.execute(drivers.select()).fetchall()

