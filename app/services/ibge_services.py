import os
import requests
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()
URL_IBGE = os.getenv("URL_IBGE")

def get_country_profile(country_code: str, lang: str = "PT"):
    url = f"{URL_IBGE}/paises/{country_code}?lang={lang}"
    print(f"Request URL: {url}")  # Log para depuração
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  # Log para depuração
    if response.status_code != 200:
        print(f"Response Content: {response.content}")  # Log para depuração
        raise HTTPException(status_code=response.status_code, detail="Erro ao acessar a API do IBGE")
    return response.json()

def get_country_indicators(country_code: str, indicator_ids: str, period: str = None):
    url = f"{URL_IBGE}/paises/{country_code}/indicadores/{indicator_ids}"
    if period:
        url += f"?periodo={period}"
    print(f"Request URL: {url}")  # Log para depuração
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  # Log para depuração
    if response.status_code != 200:
        print(f"Response Content: {response.content}")  # Log para depuração
        raise HTTPException(status_code=response.status_code, detail="Erro ao acessar a API do IBGE")
    return response.json()

def get_multiple_country_indicators(country_codes: str, indicator_ids: str = None, period: str = None):
    url = f"{URL_IBGE}/paises/{country_codes}/indicadores"
    if indicator_ids:
        url += f"/{indicator_ids}"
    if period:
        url += f"?periodo={period}"
    print(f"Request URL: {url}")  # Log para depuração
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  # Log para depuração
    if response.status_code != 200:
        print(f"Response Content: {response.content}")  # Log para depuração
        raise HTTPException(status_code=response.status_code, detail="Erro ao acessar a API do IBGE")
    return response.json()

def get_all_countries(lang: str = "PT"):
    url = f"{URL_IBGE}/paises/todos"
    url += f"?lang={lang}"
    print(f"Request URL: {url}")  # Log para depuração
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  # Log para depuração
    if response.status_code != 200:
        print(f"Response Content: {response.content}")  # Log para depuração
        raise HTTPException(status_code=response.status_code, detail="Erro ao acessar a API do IBGE")
    return response.json()

def get_all_indicators(lang: str = "PT"):
    url = f"{URL_IBGE}/paises/indicadores"
    print(f"Request URL: {url}")  # Log para depuração
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  # Log para depuração
    if response.status_code != 200:
        print(f"Response Content: {response.content}")  # Log para depuração
        raise HTTPException(status_code=response.status_code, detail="Erro ao acessar a API do IBGE")
    return response.json()
