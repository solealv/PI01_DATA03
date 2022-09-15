from typing import Optional
from pydantic import BaseModel

class Result(BaseModel):
    resultId: Optional[int]
    raceId: int 
    driverId: int 
    constructorId: int 
    number: str 
    grid: int 
    position: int 
    positionText: str 
    positionOrder: int 
    points: float 
    laps: int 
    time: str 
    milliseconds: str 
    fastestLap: str
    rank: str
    fastestLapTime: str
    fastestLapSpeed: str
    statusId: int


