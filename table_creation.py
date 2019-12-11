import mysql.connector
import config
from mysql.connector import errorcode

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

#set list of tables to be created
TABLES = {}
TABLES['tv_shows'] = ("""
     CREATE TABLE tv_shows (
      show_id int NOT NULL AUTO_INCREMENT,
      moviedb_show_id varchar(22),
      imdb_show_id varchar(22),
      name varchar(50) NOT NULL,
      popularity decimal(20,2),
      vote_count int(22),
      vote_average decimal(6,2),
      binge_release BOOLEAN,
      PRIMARY KEY (show_id)
    ) ENGINE=InnoDB""")

TABLES['tv_episodes'] = ("""
     CREATE TABLE tv_episodes (
     ep_id int NOT NULL AUTO_INCREMENT,
     show_id int NOT NULL,
     moviedb_ep_id varchar(22),
     imdb_ep_id varchar(22),
     episode_number int(22),
     season_number int(22),
     vote_count int(22),
     vote_average decimal(6,2),
     air_date varchar(20),
     PRIMARY KEY (ep_id),
     FOREIGN KEY (show_id) REFERENCES tv_shows(show_id)
    ) ENGINE=InnoDB""")


#table creation function accepts a list and exectutes each element
def table_creation(table_list):
    for table_name in table_list:
        table_description = table_list[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

#call table_creation and pass it our list of tables
table_creation(TABLES)

#close the connection
cursor.close()
cnx.close()
