from json import loads, dumps


def dataframe_to_json(dataframe):
    result = dataframe.to_json(orient="split")
    return loads(result)
