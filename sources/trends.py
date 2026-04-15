from urllib.request import urlopen
import xml.etree.ElementTree as ET

from pytrends.request import TrendReq

from config import TRENDS_LANGUAGE, TRENDS_REGIONS, TRENDS_REGION, TRENDS_TIMEZONE


REALTIME_REGION_CODES = {
    "mexico": "MX",
    "colombia": "CO",
    "spain": "ES",
    "argentina": "AR",
    "united_states": "US",
}

RSS_TRENDS_URL = "https://trends.google.com/trending/rss?geo={geo}"


def _normalize_value(value):
    if isinstance(value, dict):
        return value.get("query") or value.get("title") or str(value)

    if isinstance(value, list):
        return " ".join(str(item) for item in value if item)

    return str(value)


def _extract_topics(dataframe):
    if dataframe is None or dataframe.empty:
        return []

    if 0 in dataframe.columns:
        raw_values = dataframe[0].tolist()
    elif "title" in dataframe.columns:
        raw_values = dataframe["title"].tolist()
    elif "entityNames" in dataframe.columns:
        raw_values = dataframe["entityNames"].tolist()
    else:
        raw_values = dataframe.iloc[:, 0].tolist()

    return [
        _normalize_value(value).strip()
        for value in raw_values
        if _normalize_value(value).strip()
    ]


def _extract_rss_topics(geo_code):
    with urlopen(RSS_TRENDS_URL.format(geo=geo_code), timeout=15) as response:
        content = response.read()

    root = ET.fromstring(content)
    return [
        title.text.strip()
        for title in root.findall("./channel/item/title")
        if title is not None and title.text and title.text.strip()
    ]


def get_trending_searches():
    pytrends = TrendReq(hl=TRENDS_LANGUAGE, tz=TRENDS_TIMEZONE)
    regions = TRENDS_REGIONS or [TRENDS_REGION]
    all_topics = []
    seen = set()

    for region in regions:
        try:
            trends = pytrends.trending_searches(pn=region)
            topics = _extract_topics(trends)
        except Exception:
            realtime_code = REALTIME_REGION_CODES.get(region.lower())
            if not realtime_code:
                print(f"Aviso: Google Trends no devolvio resultados para '{region}'.")
                continue

            try:
                realtime = pytrends.realtime_trending_searches(pn=realtime_code)
                topics = _extract_topics(realtime)
            except Exception as realtime_error:
                try:
                    topics = _extract_rss_topics(realtime_code)
                    print(
                        f"Aviso: pytrends fallo para '{region}' ({realtime_code}). Se uso RSS como respaldo."
                    )
                except Exception as rss_error:
                    print(
                        f"Aviso: Google Trends fallo para '{region}' (codigo {realtime_code}): {realtime_error}. RSS tambien fallo: {rss_error}"
                    )
                    continue

        for topic in topics:
            if topic not in seen:
                seen.add(topic)
                all_topics.append(topic)

    if not all_topics:
        print("Aviso: Google Trends no esta disponible en este momento.")
        return []

    return all_topics