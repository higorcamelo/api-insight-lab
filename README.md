# API Insight Lab

## Descrição

Esta API fornece dados dos países utilizando a API do IBGE. Abaixo está um guia de navegação para ajudá-lo a entender como utilizar os diferentes endpoints.

## Endpoints

### Listar todos os países

**URL:** `/api/v1/countries`  
**Método:** `GET`  
**Descrição:** Retorna a lista de todos os países.

### Obter o perfil de um país específico

**URL:** `/api/v1/countries/{country_code}`  
**Método:** `GET`  
**Parâmetros:**
- `country_code` (string): O código ISO 3166-1 ALPHA-2 do país.

**Exemplo:** `/api/v1/countries/BR`  
**Descrição:** Retorna o perfil do país especificado.

### Obter indicadores de um país específico

**URL:** `/api/v1/countries/{country_code}/indicators/{indicator_ids}`  
**Método:** `GET`  
**Parâmetros:**
- `country_code` (string): O código ISO 3166-1 ALPHA-2 do país.
- `indicator_ids` (string): Os identificadores dos indicadores separados por pipe (|).

**Exemplo:** `/api/v1/countries/BR/indicators/77819|77820`  
**Descrição:** Retorna os indicadores especificados para o país especificado.

### Obter indicadores de um país específico para um período

**URL:** `/api/v1/countries/{country_code}/indicators/{indicator_ids}?period={period}`  
**Método:** `GET`  
**Parâmetros:**
- `country_code` (string): O código ISO 3166-1 ALPHA-2 do país.
- `indicator_ids` (string): Os identificadores dos indicadores separados por pipe (|).
- `period` (string, opcional): O período para filtrar os indicadores.

**Exemplo:** `/api/v1/countries/BR/indicators/77819|77820?period=2016`  
**Descrição:** Retorna os indicadores especificados para o país especificado no período especificado.
