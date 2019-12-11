import requests

api_key = "88b24a41df02b91de3151b904a335e9c"

def get_imbd_code(tv_id):
    url = "https://api.themoviedb.org/3/tv/" + str(tv_id) + "/external_ids?api_key=88b24a41df02b91de3151b904a335e9c&language=en-US"

    response = requests.get(url)
    data = response.json()
    imdb_id = data['imdb_id']


def update_imdb_key
