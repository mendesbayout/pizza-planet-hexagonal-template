from typing import List

from fastapi import APIRouter, Response

from api.app.adapters.dynamodb.sizeAdapter import SizeAdapter
from api.app.models.ingredient import Ingredient, IngredientCreate, IngredientUpdate
from api.app.ports.ingredient_input_port import IngredientInputPort

ingredients = APIRouter()

ingredients_port = IngredientInputPort(SizeAdapter())


@ingredients.get("/", name="get_ingredients", response_model=List[Ingredient])
async def get(response: Response):
    (ingredients_response, count) = ingredients_port.get_all()
    response.headers["X-Total-Count"] = str(count)
    return ingredients_response


@ingredients.post("/", name="create_ingredient", status_code=201, response_model=Ingredient)
async def create_contact_note(ingredient_input: IngredientCreate):
    return ingredients_port.create(ingredient_input.dict())


@ingredients.post("/{ingredient_id}", name="update_ingredient", response_model=Ingredient)
async def put(ingredient_input: IngredientUpdate):
    return ingredients_port.update(ingredient_input.dict())


@ingredients.delete("/{ingredient_id}", status_code=204, name="delete_ingredient")
async def delete_note(_id: int):
    return ingredients_port.delete(_id)
