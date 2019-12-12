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
    get_ids = ("""SELECT imdb_show_id FROM tv_shows WHERE vote_count > 5""")
    cursor.execute(get_ids)
    return cursor.fetchall()
