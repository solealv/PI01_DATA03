from fastapi import APIRouter
from config.db import conn
from models.driver import drivers

driver = APIRouter()

@driver.get('/driver')
def get_driver():
    return conn.execute(drivers.select()).fetchall()

