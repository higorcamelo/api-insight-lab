from fastapi import APIRouter, Query, HTTPException
from app.services import ibge_services

router = APIRouter()

@router.get("/countries/{country_code}")
async def read_country_profile(country_code: str, lang: str = Query("PT", description="Idioma dos dados retornados: PT, EN ou ES")):
    try:
        return ibge_services.get_country_profile(country_code, lang)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")

@router.get("/countries/{country_code}/indicators/{indicator_ids}")
async def read_country_indicators(country_code: str, indicator_ids: str, period: str = Query(None, description="Filtra os indicadores por períodos específicos")):
    try:
        return ibge_services.get_country_indicators(country_code, indicator_ids, period)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")

@router.get("/countries/indicators")
async def read_multiple_country_indicators(country_codes: str = Query(None, description="Filtra os países por seus códigos de país"), indicator_ids: str = Query(None, description="Filtra os indicadores por seus IDs específicos"), period: str = Query(None, description="Filtra os indicadores por períodos específicos")):
    try:
        return ibge_services.get_multiple_country_indicators(country_codes, indicator_ids, period)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")

@router.get("/countries")
async def read_all_countries(lang: str = "PT"):
    try:
        return ibge_services.get_all_countries()
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")

@router.get("/countries/indicators")
async def read_all_indicators():
    try:
        return ibge_services.get_all_indicators()
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")
