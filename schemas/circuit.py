from typing import Optional
from pydantic import BaseModel

class Circuit(BaseModel):
    circuitId: Optional[int]
    circuitRef: str
    name: str
    location: str
    country: str
    lat: float
    lng: float
    alt: float
    url: str