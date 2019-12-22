import requests
from bs4 import BeautifulSoup
import mysql_etl_functions

def imdb_season_1_scraper(id_list):

    for id in id_list:
        if id_list.index(id)%10 == 0:
            print("on show number " + str((id_list.index(id) + 1)) )
        page = requests.get("https://www.imdb.com/title/" + str(id[0]) +  "/episodes?season=1")
        #print(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        list = soup.find_all(class_="ipl-rating-star small")

        episode_number = 1
        if len(list):
            for item in list:
                if len(item.find_all(class_="ipl-rating-star__rating")) & len(item.find_all(class_="ipl-rating-star__total-votes")):
                    #print(item.find_all(class_="ipl-rating-star__rating"))
                    #print(item.find_all(class_="ipl-rating-star__total-votes"))
                    imdb_tuple = (id[0], id[1], episode_number, 1 ,  str(item.find_all(class_="ipl-rating-star__rating")[0].string), str(item.find_all(class_="ipl-rating-star__total-votes")[0].string.strip('()')))
                    #tuple elements are as follows: (imdb_show_id, moviedb_show_id, espisode_number, rating, total votes)
                    #print(imdb_tuple)
                    episode_number += 1
                    mysql_etl_functions.imdb_episode_rating_etl(imdb_tuple)





def imdb_paginate():
    id_list = mysql_etl_functions.get_imdb_id()
    imdb_season_1_scraper(id_list)

#imdb_paginate()
