import os
import requests
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()
URL_IBGE = os.getenv("URL_IBGE")

def get_country_profile(country_codes: str, lang: str = "PT"):
    url = f"{URL_IBGE}/{country_codes}?lang={lang}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erro ao acessar a API do IBGE")
    return response.json()

def get_country_indicators(country_codes: str, indicator_ids: str, period: str = None):
    url = f"{URL_IBGE}/{country_codes}/indicadores/{indicator_ids}"
    if period:
        url += f"?periodo={period}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erro ao acessar a API do IBGE")
    return response.json()
