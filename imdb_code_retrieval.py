import requests
import mysql_etl_functions

api_key = "88b24a41df02b91de3151b904a335e9c"

def get_imbd_code(tv_id):
    #takes a moviedb_id for a tv show and returns the associated imdb_id
    url = "https://api.themoviedb.org/3/tv/" + str(tv_id) + "/external_ids?api_key=88b24a41df02b91de3151b904a335e9c&language=en-US"
    response = requests.get(url)
    #print(response)
    data = response.json()
    imdb_id = data['imdb_id']
    #print(imdb_id)
    return imdb_id


def update_imdb_key():
    #wrapper function to add imdb keys to the DB. currently set up to only update shows that have more that 5 votes on moviedb

    mdb_id_list = mysql_etl_functions.get_moviedb_id()
    #get list of movie_db_ids

    print('mdb ids retrieved')

    for id in mdb_id_list:
        #and loop through them

        tuple = (get_imbd_code(id[0]), id[0])
        print(tuple)

        mysql_etl_functions.update_imdb_id(tuple)

#update_imdb_key()
