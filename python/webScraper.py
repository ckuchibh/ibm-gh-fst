from bs4 import BeautifulSoup as bs 

import requests

response = requests.get("https://www.training-support.net/webelements/tables")
webpage_content = response.content

soup = bs(webpage_content,"html.parser")

table = soup.find('table')

# this is not an error
for tr in table.find_all("tr"):
    cells = tr.find_all('td') if tr.find_all('td') else tr.find_all('th')
    rows = [i.text for i in cells]
    print(rows)