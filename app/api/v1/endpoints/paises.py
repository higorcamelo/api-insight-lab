from fastapi import APIRouter, HTTPException, Query
from app.services.ibge_service import get_countries, get_country_profile, get_country_indicators

router = APIRouter()

@router.get("/countries")
def list_countries(lang: str = "PT"):
    try:
        return get_countries(lang)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/countries/{country_codes}")
def get_profile(country_codes: str, lang: str = "PT"):
    try:
        return get_country_profile(country_codes, lang)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/countries/{country_codes}/indicators/{indicator_ids}")
def get_indicators(country_codes: str, indicator_ids: str, period: str = None):
    try:
        return get_country_indicators(country_codes, indicator_ids, period)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
