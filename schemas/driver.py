from typing import Optional
from pydantic import BaseModel

class Driver(BaseModel):
    driverId: Optional[int]
    driverRef: str
    num: int 
    code: str
    name: str
    dob: str
    nationality: str
    url: str