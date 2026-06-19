import pandas as pd

dataframe = pd.read_excel("VehicleExcel.xlsx",sheet_name="Sheet1")
print(dataframe)
print("Rows, Cols => ",dataframe.shape)
print(dataframe[""])

