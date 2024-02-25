def dataframe_to_json(dataframe):
    return dataframe.to_json("rcvs.json", orient="columns")
