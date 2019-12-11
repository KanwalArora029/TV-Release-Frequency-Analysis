import mysql.connector
import config

DB_NAME = 'tv_shows'


cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = DB_NAME,
    use_pure=True
)


def show_etl(show, binge_release):
    cursor = cnx.cursor()

    add_show = 



def db_insert(cnx, cursor, parsed_results):
    add_business = ("""INSERT INTO yelp_reviews
               (review_id, business_id, reviews, time_created)
               VALUES (%s, %s, %s, %s)""")
    cursor.executemany(add_business, parsed_results)
    cnx.commit()
    print('Good job!')
