from pydantic import BaseModel
from typing import Optional

class RehberBase(BaseModel):
    Name: str
    Surname: str
    Number: str
    Adress: str

class RehberCreate(RehberBase):
    pass

class RehberUpdate(BaseModel):
    Name: Optional[str] = None
    Surname: Optional[str] = None
    Number: Optional[str] = None
    Adress: Optional[str] = None

class RehberResponse(RehberBase):
    id: int

    class Config:
        orm_mode = True
