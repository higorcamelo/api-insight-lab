from fastapi import APIRouter, HTTPException
from app.services.ibge_services import get_country_profile, get_country_indicators

router = APIRouter()

@router.get("/countries/{country_codes}")
def read_country_profile(country_codes: str, lang: str = "PT"):
    return get_country_profile(country_codes, lang)

@router.get("/countries/{country_codes}/indicators/{indicator_ids}")
def read_country_indicators(country_codes: str, indicator_ids: str, period: str = None):
    return get_country_indicators(country_codes, indicator_ids, period)
