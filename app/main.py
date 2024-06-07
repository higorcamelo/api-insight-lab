from fastapi import FastAPI, Query
from .services.ibge_services import get_country_profile, get_country_indicators

app = FastAPI(title="API Insight Lab", description="API que fornece dados dos países utilizando a API do IBGE.", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Bem vindo(a) a API do IBGE! Feito via FastAPI para o Insight Lab! :)"}

@app.get("/api/v1/countries/{country_code}", summary="Obter o perfil de um país específico", description="Retorna o perfil do país especificado pelo código ISO 3166-1 ALPHA-2.")
async def read_country_profile(country_code: str, lang: str = Query("PT", description="Idioma dos dados retornados: PT (Português), EN (Inglês), ES (Espanhol)")):
    return get_country_profile(country_code, lang)

@app.get("/api/v1/countries/{country_code}/indicators/{indicator_ids}", summary="Obter indicadores de um país específico", description="Retorna os indicadores especificados para o país especificado.")
async def read_country_indicators(country_code: str, indicator_ids: str, period: str = Query(None, description="Filtra os indicadores por períodos específicos.")):
    return get_country_indicators(country_code, indicator_ids, period)