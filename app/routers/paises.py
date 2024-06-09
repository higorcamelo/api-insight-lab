from fastapi import APIRouter, Query, HTTPException
from app.services import ibge_services

router = APIRouter()

@router.get("/countries/{country_code}", summary="Obter perfil de um país", description="Retorna informações detalhadas sobre um país específico, incluindo dados geográficos, políticos e históricos.")
async def read_country_profile(
    country_code: str, 
    lang: str = Query("PT", description="Idioma dos dados retornados: PT (Português), EN (Inglês) ou ES (Espanhol)")
):
    try:
        return ibge_services.get_country_profile(country_code, lang)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")

@router.get("/countries/{country_code}/indicators/{indicator_ids}", summary="Obter indicadores específicos de um país", description="Retorna indicadores socioeconômicos e ambientais específicos de um país, organizados em uma série e em valores numéricos.")
async def read_country_indicators(
    country_code: str, 
    indicator_ids: str, 
    period: str = Query(None, description="Filtra os indicadores por períodos específicos")
):
    try:
        return ibge_services.get_country_indicators(country_code, indicator_ids, period)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")

@router.get("/countries/{country_code}/indicators", summary="Obter múltiplos indicadores para um ou mais países", description="Retorna múltiplos indicadores disponíveis sobre um país específico, filtrados por períodos opcionais.")
async def read_multiple_country_indicators(
    country_codes: str = Query(None, description="Filtra os países por seus códigos de país"), 
    period: str = Query(None, description="Filtra os indicadores por períodos específicos")
):
    try:
        return ibge_services.get_multiple_country_indicators(country_codes, period)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")

@router.get("/countries", summary="Obter lista de todos os países disponíveis", description="Retorna uma lista de todos os países disponíveis na API do IBGE.")
async def read_all_countries(
    lang: str = Query("PT", description="Idioma dos dados retornados: PT (Português), EN (Inglês) ou ES (Espanhol)")
):
    try:
        return ibge_services.get_all_countries(lang)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")  # Log para depuração
        raise HTTPException(status_code=500, detail="Erro inesperado")
