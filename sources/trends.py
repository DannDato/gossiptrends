from pytrends.request import TrendReq

from config import TRENDS_LANGUAGE, TRENDS_REGION, TRENDS_TIMEZONE

def get_trending_searches():
    pytrends = TrendReq(hl=TRENDS_LANGUAGE, tz=TRENDS_TIMEZONE)
    trends = pytrends.trending_searches(pn=TRENDS_REGION)

    return trends[0].tolist()