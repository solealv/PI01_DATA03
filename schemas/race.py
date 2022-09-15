from typing import Optional
from pydantic import BaseModel

class Race(BaseModel):
    raceId: Optional[int]
    year: int 
    round: int 
    circuitId: int 
    name: str 
    date: str
    time: str 
    url: str