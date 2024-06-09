## Descrição

Esta API fornece dados dos países utilizando a API do IBGE. Abaixo está um guia de navegação para ajudá-lo a entender como utilizar os diferentes endpoints.

## Endpoints

### Obter o perfil de um país específico

**URL:** `/api/v1/countries/{country_code}`  
**Método:** `GET`  
**Parâmetros:**
- `country_code` (string): O código ISO 3166-1 ALPHA-2 do país.
- `lang` (string, opcional): Idioma dos dados retornados: PT (Português), EN (Inglês) ou ES (Espanhol). Valor padrão é PT.

**Exemplo:** `/api/v1/countries/BR`  
**Descrição:** Retorna informações detalhadas sobre um país específico, incluindo dados geográficos, políticos e históricos.

### Obter indicadores de um país específico

**URL:** `/api/v1/countries/{country_code}/indicators/{indicator_ids}`  
**Método:** `GET`  
**Parâmetros:**
- `country_code` (string): O código ISO 3166-1 ALPHA-2 do país.
- `indicator_ids` (string): Os identificadores dos indicadores separados por pipe (|).
- `period` (string, opcional): Filtra os indicadores por períodos específicos.

**Exemplo:** `/api/v1/countries/BR/indicators/77819|77820`  
**Descrição:** Retorna indicadores socioeconômicos e ambientais específicos de um país, organizados em uma série e em valores numéricos.

### Obter indicadores de múltiplos países

**URL:** `/api/v1/countries/indicators`  
**Método:** `GET`  
**Parâmetros:**
- `country_codes` (string, opcional): Filtra os países por seus códigos de país, separados por pipe (|).
- `period` (string, opcional): Filtra os indicadores por períodos específicos.

**Exemplo:** `/api/v1/countries/indicators?country_codes=BR|AR&period=2016`  
**Descrição:** Retorna múltiplos indicadores disponíveis sobre um país específico, filtrados por períodos opcionais.

### Obter lista de todos os países disponíveis

**URL:** `/api/v1/countries`  
**Método:** `GET`  
**Parâmetros:**
- `lang` (string, opcional): Idioma dos dados retornados: PT (Português), EN (Inglês) ou ES (Espanhol). Valor padrão é PT.

**Exemplo:** `/api/v1/countries`  
**Descrição:** Retorna uma lista de todos os países disponíveis na API do IBGE.

## Docker

### Construir a imagem Docker

Para construir a imagem Docker da aplicação, utilize o seguinte comando:

```sh
docker build -t api-insight-lab .
```
### Executar o container Docker

Para executar o container Docker, utilize o seguinte comando:

```sh

docker run -d -p 8000:8000 --name api-insight-lab-container api-insight-lab

```

### Parar e remover o container Docker

Quando quiser parar e remover o container, utilize os seguintes comandos:

```sh

docker stop api-insight-lab-container
docker rm api-insight-lab-container
```