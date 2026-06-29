# import json
# from locale import currency

# with open("Example.json") as myJson:
#     data = myJson.read()

# obj = json.loads(data)

# for root,unit in obj.items():
#     if type(unit) == dict:
#         for item1,item2 in unit.items():
#             print(f"{root} => {item1}, {item2}")


import pandas as pd

df = pd.read_json("Example.json",orient="index")
print(df)
