from json import loads, dumps

from src import rcvs_web_scraper

df = rcvs_web_scraper.df

result = df.to_json(orient="split")
parsed = loads(result)
dumps(parsed, indent=4)