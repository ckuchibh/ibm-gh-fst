from numpy._core.numeric import False_
import pandas as pd

dataframe = pd.read_csv("Users.csv")
print(dataframe)
print("-"*50)
print(dataframe["Username"])

print("-"*50)
print(dataframe["Username"][1])

print("-"*50)
print(dataframe.sort_values("Username"))

print("-"*50)
print(dataframe.sort_values("Passwords",ascending=False))
