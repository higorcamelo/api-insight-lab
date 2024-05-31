from fastapi import APIRouter, HTTPException, Query
from app.services.ibge_service import get_countries, get_country_profile, get_country_indicators

router = APIRouter()

@router.get("/countries")
def read_countries(lang: str = "PT"):
    return get_countries(lang)

@router.get("/countries/{country_codes}")
def read_country_profile(country_codes: str, lang: str = "PT"):
    return get_country_profile(country_codes, lang)

@router.get("/countries/{country_codes}/indicators/{indicator_ids}")
def read_country_indicators(country_codes: str, indicator_ids: str, period: str = None):
    return get_country_indicators(country_codes, indicator_ids, period)