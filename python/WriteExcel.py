# Import pandas, ExcelFile and ExcelWriter
from csv import writer
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
 
# Structure our data as a dictionary
data = {
  "Vehicle Type": ["Car", "Car", "Bike"],
  "Manufacturer": ["Maruti", "Toyota", "Royal Enfield"],
  "Model": ["Swift", "Corolla", "Thunderbird"]
}
 
dataframe = pd.DataFrame(data)
print(dataframe)

writer = ExcelWriter('VehicleExcel.xlsx')
dataframe.to_excel(writer,sheet_name="Sheet1",index=False)

writer.close()