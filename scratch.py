import requests
import time

url = "https://api.themoviedb.org/3/discover/tv/"

api_key = "88b24a41df02b91de3151b904a335e9c"

start_date = '2019-01-01'
sort_by = 'popularity.desc'

def show_paginate(start_date, end_date):
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
        show_list = get_shows(start_date, (page + 1))

def get_shows(start_date, page, counter = 0):
    #takes in a date range and a page number

    if counter >= 10:
        #this if statement is here to prevent infinite recursion
        print('Error: to many recurisve attempts. Aborting')
        return

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
            #steps through each show in the page and builds a dict from the results

            temp_dict = {'show_id': show['id']
            ,'name': show['name']
            ,'popularity': show['popularity']
            ,'vote_count': show['vote_count']
            ,'vote_average': show['vote_average']
            }

            show_list.append(temp_dict)

        return show_list

    except:
        counter += 1
        print('waiting...' + str(counter))
        time.sleep(2)
        #wait 2 seconds and then call the same function again
        return get_shows(start_date, page, counter)

return_list = get_shows(start_date, 1)
#show_paginate(start_date, end_date)

print(return_list)