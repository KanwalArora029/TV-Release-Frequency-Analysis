import mysql.connector
import config

#set database name
DB_NAME = 'tv_shows'

#create connection
cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = DB_NAME,
    use_pure=True
)

#start cursor
cursor = cnx.cursor()


def show_etl(parsed_results):
    #inserts new shows
    add_show = ("""INSERT INTO tv_shows
               (moviedb_show_id, name, popularity, vote_count, vote_average, binge_release)
               VALUES (%s, %s, %s, %s, %s, %s)""")
    cursor.execute(add_show, parsed_results)
    cnx.commit()


def ep_etl(parsed_results):
    #inserts new episodes
    add_ep = ("""INSERT INTO tv_episodes
               (moviedb_ep_id, moviedb_show_id, episode_number, vote_count, vote_average, air_date)
               VALUES (%s, %s, %s, %s, %s, %s)""")
    cursor.execute(add_ep, parsed_results)
    cnx.commit()

def imdb_episode_rating_etl(parsed_results):
    add_ep = ("""INSERT INTO imdb_episode_rating
               (imdb_show_id, moviedb_show_id, episode_number, season_number, imdb_rating, imdb_vote_count)
               VALUES (%s, %s, %s, %s, %s, %s)""")
    cursor.execute(add_ep, parsed_results)
    cnx.commit()

def get_moviedb_id():
    #simply returns all movie_db_id from the database who more than 5 votes
    get_ids = ("""SELECT moviedb_show_id FROM tv_shows WHERE vote_count > 5""")
    cursor.execute(get_ids)
    return cursor.fetchall()

def update_imdb_id(id_tuple):
    #takes a list of 2 element tuples, first element is imdb_id and the second is the movie_db_id
    update_imdb = ("""UPDATE tv_shows SET imdb_show_id = %s WHERE moviedb_show_id = %s """)
    cursor.execute(update_imdb, id_tuple)
    cnx.commit()

def get_imdb_id():
    #gets list of tv show imdb ids if the show has more than 5 votes
    get_ids = ("""SELECT imdb_show_id, moviedb_show_id FROM tv_shows WHERE imdb_show_id IS NOT NULL AND vote_count > 5""")
    cursor.execute(get_ids)
    return cursor.fetchall()

def get_data_frame():

    get_data = '''SELECT rate.episode_id
                    ,tv.binge_release
                	,tv.name
                    ,rate.episode_number
                	,rate.imdb_vote_count
                    ,rate.imdb_rating
                    ,ep.vote_count AS moviedb_vote_count
                    ,ep.vote_average AS moviedb_vote_rating
                FROM tv_shows.imdb_episode_rating rate
                LEFT JOIN tv_shows.tv_shows tv ON rate.moviedb_show_id = tv.moviedb_show_id
                LEFT JOIN tv_shows.tv_episodes ep ON(rate.moviedb_show_id = ep.moviedb_show_id AND rate.episode_number = ep.episode_number)
                WHERE rate.imdb_vote_count > 0'''

    cursor.execute(get_data)
    return cursor.fetchall()
