from fastapi import APIRouter
from config.db import conn
from models.result import results
from schemas.result import Result

result = APIRouter()

@result.get('/result', response_model=list[Result])
def get_reult():
    return conn.execute(results.select()).fetchall()
