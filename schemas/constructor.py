from typing import Optional
from pydantic import BaseModel

class Constructor(BaseModel):
    constructorId: Optional[int]
    constructorRef: str
    name: str
    nationality: str
    url: str