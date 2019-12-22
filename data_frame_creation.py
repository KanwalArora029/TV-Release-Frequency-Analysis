#final data structuring step where we query data from MySQL and add some final touches to get it chart ready

import mysql_etl_functions
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def create_TV_data_frames():
    '''this function queries the established MySQL data base and returns a
    finalized list of dataframe objects. The list is of the following form:
    [df, df_first_10, first_10_binge, first_10_serial] where the 10 indicates
    that only the first 10 episodes of a given series are included and
    binge/serial denotes release type'''

    data =  mysql_etl_functions.get_data_frame()
    #retrieve data stored in MySQL

    df = pd.DataFrame(data , columns = ['id', 'binge_release', 'show_name', 'episode', 'imdb_votes', 'imdb_score', 'moviedb_votes', 'moviedb_score'])
    #turn it into a Pandas dataframe

    df = df.set_index('id')
    #set the index to the MySQL supplied one

    map_dict = {1: 'Batch', 0 : 'Serial'}
    df['binge_release'] = df['binge_release'].replace(map_dict)
    #change the Boolean 'binge release' field values into more interpretable terms

    df['imdb_score'] = df['imdb_score'].astype('float')
    df['moviedb_score'] = df['moviedb_score'].astype('float')
    #and finally turn both score values into floats

    df_first_10 = df[df['episode'] < 11]
    #make a subset of only the first 10 episodes of a given series

    first_10_binge = df[df['binge_release'] == 'Batch']
    first_10_serial = df[df['binge_release'] == 'Serial']
    #then split that subset up by 'binge_release' type

    return [df, df_first_10, first_10_binge, first_10_serial]

'''episode_count_data = mysql_etl_functions.get_episode_count()
df_ep_count = pd.DataFrame(episode_count_data , columns = ['episode_number','total_batch', 'total_serial'])
df_ep_count['total_batch'] = df_ep_count['total_batch'].astype('int')
df_ep_count['total_serial'] = df_ep_count['total_serial'].astype('int')'''
