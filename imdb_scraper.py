import requests
from bs4 import BeautifulSoup
import mysql_etl_functions

'''page = requests.get("https://www.imdb.com/title/tt8111088/episodes?season=1")
soup = BeautifulSoup(page.content, 'html.parser')
list = soup.find_all(class_="ipl-rating-star small")
print(list[0])
for item in list:
    print(item.find_all(class_="ipl-rating-star__rating")[0].string)
    print(item.find_all(class_="ipl-rating-star__total-votes")[0].string)'''


def imdb_season_1_scraper(id_list):

    for id in id_list:
        print(id)
        page = requests.get("https://www.imdb.com/title/" + str(id) +  "/episodes?season=1")
        print(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        list = soup.find_all(class_="ipl-rating-star small")

        for item in list:
            print(item.find_all(class_="ipl-rating-star__rating")[0].string)
            print(item.find_all(class_="ipl-rating-star__total-votes")[0].string)


def imdb_paginate():
    id_list = mysql_etl_functions.get_imdb_id()
    imdb_season_1_scraper(id_list)

imdb_paginate()
