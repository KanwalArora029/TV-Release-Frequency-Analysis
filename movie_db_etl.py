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

    add_show = ("""INSERT INTO tv_shows
               (moviedb_show_id, name, popularity, vote_count, vote_average, binge_release)
               VALUES (%s, %s, %s, %s, %s, %s)""")
    cursor.execute(add_show, parsed_results)
    cnx.commit()


def ep_etl(parsed_results):

    add_ep = ("""INSERT INTO tv_episodes
               (moviedb_ep_id, moviedb_show_id, episode_number, vote_count, vote_average, air_date)
               VALUES (%s, %s, %s, %s, %s, %s)""")
    cursor.execute(add_ep, parsed_results)
    cnx.commit()
