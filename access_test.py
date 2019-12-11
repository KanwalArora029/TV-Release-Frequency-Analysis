import requests
import time
import movie_db_etl
#import movie_db_etl

api_key = "88b24a41df02b91de3151b904a335e9c"

start_date = '2019-01-01'
sort_by = 'popularity.desc'

def show_paginate(start_date):
    url = "https://api.themoviedb.org/3/discover/tv/"
    #This initial call is just to get the numbers of pages we'll need to paginate through
    url_params = {
                    'first_air_date.gte': start_date,
                    'sort_by': sort_by,
                    'api_key' : api_key
                }
    response = requests.get(url, params=url_params)
    data = response.json()
    page_count = data['total_pages']
    #set the page count
    #then loop through each page
    for page in range(page_count):
        #get a list of shows from each page
        show_list = get_shows(start_date, (page + 1))
        #loop through each show in the page
        for show in show_list:
            #get a list of season 1 episodes for the show
            episode_list = get_first_season(show[0])
            #if statement checks to assure there are valid eposides associated with a show. If there are no episodes the show is not included
            if len(episode_list):
                first_date = episode_list[0][-1]
                last_date = episode_list[-1][-1]
                #check for "binge release" to see if the release date of the first episode matches the last
                show = show +  ((first_date == last_date),)
                movie_db_etl.show_etl(show)

                for episode in episode_list:
                    movie_db_etl.ep_etl(episode)

    return



def get_shows(start_date, page, counter = 0):
    #takes in a date range and a page number

    url = "https://api.themoviedb.org/3/discover/tv/"

    url_params = {
                    'first_air_date.gte': start_date,
                    'sort_by': sort_by,
                    'api_key' : api_key,
                    'page' : page
                }
    try:
        #the moviedb limits your calls to 40 per 10 seconds. This try/except will reattempt in case of exceeding limit
        results = requests.get(url, params=url_params).json()['results']
        show_list = []
        temp_dict = {}
        for show in results:
            #steps through each show in the page and builds a tuple from the results

            show_tuple = (show['id'], show['name'], show['popularity'], show['vote_count'], show['vote_average'])

            show_list.append(show_tuple)

        return show_list

    except:
        if counter >= 10:
            #this if statement is here to prevent infinite recursion
            print('Error: to many recurisve calls for get_shows(). Aborting')
            return
        counter += 1
        print('waiting...' + str(counter))
        time.sleep(2)
        #wait 2 seconds and then call the same function again
        return get_shows(start_date, page, counter)

#return_list = get_shows(start_date, 1)
#print(return_list)
#show_paginate(start_date, end_date)

#print(return_list)

add_ep = ("""INSERT INTO tv_episodes
           (moviedb_ep_id, moviedb_show_id, episode_number, vote_count, vote_average, air_date)
           VALUES (%s, %s, %s, %s, %s)""")

def get_first_season(show_id, counter = 0):
    url = 'https://api.themoviedb.org/3/tv/' + str(show_id) + '/season/1?api_key=88b24a41df02b91de3151b904a335e9c&language=en-US'

    try:
        results = requests.get(url).json()['episodes']
        episode_list = []
        for episode in results:
            episode_tuple = (episode['id'], show_id, episode['episode_number'], episode['vote_count'], episode['vote_average'], episode['air_date'])
            episode_list.append(episode_tuple)
        return episode_list

    except:
        if counter >= 10:
            #this if statement is here to prevent infinite recursion
            print('Error: to many recurisve calls for get_first_season(). Aborting')
            return
        counter += 1
        print('waiting...' + str(counter))
        time.sleep(2)
        #wait 2 seconds and then call the same function again
        return get_first_season(show_id ,counter)

#print(get_first_season(82856))

show_paginate(start_date)
