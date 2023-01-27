from fastapi import APIRouter

from api.app.adapters.dynamodb.sizeAdapter import SizeAdapter
from api.app.ports.size_input_port import SizeInputPort

size_router = APIRouter()

size_input_port = SizeInputPort(SizeAdapter())


@size_router.get("/")
async def get_all_sizes():
    sizes, count = size_input_port.get_all()
    return {"sizes": sizes, "count": count}


@size_router.get("/{size_id}")
async def get_size(size_id: str):
    size = size_input_port.get_by_id(size_id)
    if size:
        return {"size": size}
    else:
        return {"message": "Size not found"}


@size_router.post("/")
async def create_size(size: dict):
    new_size = size_input_port.create(size)
    return {"size": new_size}


@size_router.put("/{size_id}")
async def update_size(size: dict):
    updated_size = size_input_port.update(size)
    if updated_size:
        return {"size": updated_size}
    else:
        return {"message": "Size not found"}


@size_router.delete("/{size_id}")
async def delete_size(size_id: int):
    size_input_port.delete(size_id)
    return {"message": "Size deleted"}
