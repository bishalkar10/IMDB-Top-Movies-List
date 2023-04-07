import requests
from bs4 import BeautifulSoup
import pandas as pd


url = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
soup = BeautifulSoup(url.text, "lxml")

heading = soup.find_all('th')[1:3]
column = [item.text for item in heading]
column.insert(1, "Year")
print(column)

titleColumn = soup.find_all("td", class_="titleColumn")
names = [item.a.text for item in titleColumn]
# print(names[2])
# print(type(names[2]))
year = [item.span.text[1:-1] for item in titleColumn]
# print(year)
ratings = soup.find_all("td", class_="ratingColumn imdbRating")
# print(type(ratings))
# print(ratings)
rating_list = [float(item.strong.text) for item in ratings]
# print(rating_list)
# for item in rating_list:
#     print(item)

data = list(zip(names, year, rating_list))
print(data)
table = pd.DataFrame(data, columns=column)
print(table)
