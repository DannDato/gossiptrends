# Gossip Topic

Script en Python para detectar temas de tecnologia combinando Google Trends y publicaciones populares de Reddit, con filtrado por palabras clave.

## Requisitos

- Python 3.10 o superior
- Dependencias instaladas: `praw` y `pytrends`
- Credenciales de Reddit si quieres incluir esa fuente

## Instalacion

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Configuracion

El proyecto lee variables desde el archivo `.env` en la raiz.

Variables disponibles:

```env
ENABLE_REDDIT=false
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=gossip-topic-finder
REDDIT_SUBREDDITS=technology,programming,gadgets,artificial
REDDIT_POST_LIMIT=10
TRENDS_LANGUAGE=es-MX
TRENDS_TIMEZONE=360
TRENDS_REGIONS=mexico,colombia,spain,argentina
```

Notas:

- Si `ENABLE_REDDIT=false`, el proyecto no intenta usar Reddit.
- Si `ENABLE_REDDIT=true` pero `REDDIT_CLIENT_ID` o `REDDIT_CLIENT_SECRET` estan vacios, la fuente de Reddit se omite.
- `REDDIT_SUBREDDITS` acepta una lista separada por comas.
- `TRENDS_TIMEZONE` y `REDDIT_POST_LIMIT` deben ser enteros.
- `TRENDS_REGIONS` acepta una lista separada por comas y se consulta en orden.
- Para `TRENDS_REGIONS`, usa nombres esperados por `pytrends` como `mexico`, `colombia`, `spain`, `argentina`.

## Uso

```bash
python main.py
```

El script:

1. Consulta tendencias de Google Trends.
2. Consulta posts populares de los subreddits configurados.
3. Une los resultados y filtra temas relacionados con tecnologia.
4. Imprime las primeras 10 ideas.

## Estructura

```text
main.py
config.py
sources/
  reddit.py
  trends.py
utils/
  filter.py
```

## Pendiente recomendable

- Mover tambien `TECH_KEYWORDS` a configuracion si quieres ajustar el filtro sin tocar codigo.
- Fijar dependencias en un `requirements.txt` si vas a compartir o desplegar el proyecto.