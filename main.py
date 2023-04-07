# importing the necessary modules to work with
import requests
from bs4 import BeautifulSoup
import pandas as pd

# using the 'request' module to fetch the url that we are gonna scrape
url = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
# using the 'lxml' parser to parse the html
soup = BeautifulSoup(url.text, "lxml")

# we will get for elements inside the list. The left most and the right most elements are empty
heading = soup.find_all('th')[1:3]
column = [item.text for item in heading]
column.insert(1, "Year")  # inserting the 'Year' element inside the list
# print(column)
titleColumn = soup.find_all("td", class_="titleColumn")
names = [item.a.text for item in titleColumn]
# print(names[2])
# print(type(names[2]))
year = [item.span.text[1:-1] for item in titleColumn]
# print(year)
ratings = soup.find_all("td", class_="ratingColumn imdbRating")
# print(ratings)
rating_list = [float(item.strong.text) for item in ratings]
# print(rating_list)
list_items = (names, year, rating_list)
data = {key: value for key, value in zip(column, list_items)}

table = pd.DataFrame(data)
print(table)
# table.to_csv("table.csv", index=False)
