from fastapi import FastAPI
from api.v1.endpoints import paises

app = FastAPI()

app.include_router(paises.router, prefix="/api/v1", tags=["countries"])