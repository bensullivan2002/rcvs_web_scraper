from json import loads, dumps

df = src.rcvs_web_scraper.df

result = df.to_json(orient="split")
parsed = loads(result)
dumps(parsed, indent=4)
