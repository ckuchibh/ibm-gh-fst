import pandas as pd

dataframe = pd.read_csv("Data.csv")
print(dataframe)
print()
print(dataframe["Name"][2])