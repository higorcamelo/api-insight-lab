from fastapi import FastAPI
from app.routers import paises
import logging

logging.basicConfig(level=logging.DEBUG)
app = FastAPI(title="API Insight Lab", description="API que fornece dados dos países utilizando a API do IBGE.", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Bem vindo(a) a API do IBGE! Feito via FastAPI para o Insight Lab! :)"}

app.include_router(paises.router, prefix="/api/v1")
