import mysql_etl_functions
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data =  mysql_etl_functions.get_data_frame()

df = pd.DataFrame(data , columns = ['id', 'binge_release', 'show_name', 'episode', 'imdb_votes', 'imdb_score', 'moviedb_votes', 'moviedb_score'])
df = df.set_index('id')
map_dict = {1: 'yes', 0 : 'no'}
df['binge_release'] = df['binge_release'].replace(map_dict)
df['imdb_score'] = df['imdb_score'].astype('float')
df['moviedb_score'] = df['moviedb_score'].astype('float')


df_first_10 = df[df['episode'] < 11]
first_10_binge = df[df['binge_release'] == 'yes']
first_10_serial = df[df['binge_release'] == 'no']



def hist_plot():
    fig = plt.figure()
    sns.set_palette('colorblind')
    hist_binge = sns.distplot(first_10_binge['imdb_score'], kde = False)
    hist_serial = sns.distplot(first_10_serial['imdb_score'], kde = False)
    fig.legend(labels=['binge','serial'])
    plt.show()

def box_plot():
    fig = plt.figure()
    sns.set_palette('colorblind')
    cat = sns.catplot(x="episode", y="imdb_score", hue="binge_release", data=df, kind="box")
    plt.show()

#box_plot()

def simple_box_plot():
    fig = plt.figure()
    sns.set_palette('colorblind')
    ax = sns.boxplot(x= 'binge_release', y = 'imdb_score', data = df)
    plt.show()

simple_box_plot()
