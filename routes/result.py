from fastapi import APIRouter
from config.db import conn
from models.result import results

result = APIRouter()

@result.get('/result')
def get_reult():
    return conn.execute(results.select()).fetchall()
