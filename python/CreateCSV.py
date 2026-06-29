import pandas as pd

data = {
    "Vehicle Type": ["Car", "Car", "Bike"],
  "Manufacturer": ["Maruti", "Toyota", "Royal Enfield"],
  "Model": ["Swift", "Corolla", "Thunderbird"]
}

dataframe = pd.DataFrame(data)

dataframe.to_csv("CreatedCsvVehicle.csv",index=False)