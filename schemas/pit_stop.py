from typing import Optional
from pydantic import BaseModel

class Pit_stop(BaseModel):
    raceId: int 
    driverId: int 
    stop: int 
    lap: int 
    time: str 
    duration: float 
    milliseconds: int