import pandas as pd

data = [
    [1,2,3,4],
    ["Narayan","Shruthi","Sarang","Manish"],
    ["Center","Left","Right","Extreme-Right"]
]

df = pd.DataFrame(data,
columns=["Classmate1","Classmate2","Classmate3","Classmate4"],
index=["S.no","Name","Position"]).T


df.to_xml("Classmates.xml",index=False,row_name="Classmate")