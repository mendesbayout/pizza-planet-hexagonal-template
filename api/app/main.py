import sys

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.app.utils.exceptions import ItemNotFoundError

from .config.env_manager import get_settings
from .events.register import register_routers
from starlette.middleware.cors import CORSMiddleware

EnvManager = get_settings()

app = FastAPI(title="Pizza Planet")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'] if EnvManager.is_dev() else [],
    allow_origin_regex=EnvManager.ALLOW_ORIGIN_REGEX,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['X-Total-Count']
)

register_routers(app, "app.routers", "api")


@app.get("/")
async def get():
    return {"api": "clients api", "version": "0.1", "backend": "lambda"}


@app.exception_handler(ItemNotFoundError)
async def unicorn_exception_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! {exc.error_msg}, {request.method}"},
    )
