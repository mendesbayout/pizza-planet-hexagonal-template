from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str
    price: float


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(IngredientBase):
    _id: int


class Ingredient(IngredientBase):
    _id: int
    creation_date: int
    updated_date: int = 0
