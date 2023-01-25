from pydantic import BaseModel

class SizeBase(BaseModel):
    name: str
    price: float

class SizeCreate(SizeBase):
    pass

class SizeUpdate(SizeBase):
    _id: int

class Size(SizeBase):
    _id: int
