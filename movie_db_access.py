import requests

url = "https://api.themoviedb.org/3/discover/tv/"

api_key = "88b24a41df02b91de3151b904a335e9c"

start_date = '2019-01-01'
end_date = '2019-11-30'
sort_by = 'popularity.desc'

url_params = {
                'air_date.gte': start_date,
                'air_date.lte': end_date,
                'sort_by': sort_by,
                'api_key' : api_key,
                'page' : 1
            }


response = requests.get(url, params=url_params)

data = response.json()
print(data)
total_pages = data['total_pages']
print(total_pages)
show_list = []

print(data)
for item in data:
    print(item)
print(data['results'][0])
print(len(data['results'][0]))
for show in data['results']:
    temp_dict = {'show_id': show['id']
    ,'name': show['name']
    ,'popularity': show['popularity']
    ,'vote_count': show['vote_count']
    ,'vote_average': show['vote_average']
    }
    show_list.append(temp_dict)
print(show_list)
