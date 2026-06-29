import pandas as pd 

data = {
    "Username":["Admin","Charles","Deku"],
    "Passwords":["password","Chalr13","AllMight"]
}

dataframe = pd.DataFrame(data)

dataframe.to_csv("Users.csv",index=False)
