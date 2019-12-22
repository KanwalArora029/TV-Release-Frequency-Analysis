import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import data_frame_creation

df_list = data_frame_creation.create_TV_data_frames()
df = df_list[0]
df_first_10 = df_list[1]
first_10_binge = df_list[2]
first_10_serial = df_list[3]
#initial code in place to call the dataframe creation function and get the set of dataframes we need

def dual_hist_plot(df_1, df_2):
    #takes in two dataframes and returns a dual histogram of both layered on top of eachother
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    hist_serial = sns.distplot(df_1['imdb_score'], kde = False)
    hist_binge = sns.distplot(first_10_binge['imdb_score'], kde = False)
    fig.legend(labels=['Serial','Batch'])
    hist_serial.set_xlabel('IMDb Score')
    plt.show()

def box_plot(df):
    #takes in a dataframe and returns of a box and whisker plot of imdb score by episode
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns.catplot(x="episode", y="imdb_score", hue="binge_release", data=df, kind="box")
    ax.set_axis_labels("Episode Number", "IMDb Score")
    plt.title('Score by Episode')
    ax._legend.set_title('Release Type')
    plt.show()

#box_plot()

def simple_box_plot(df):
    #takes a dataframe and creates a two-part box and whisker grouping the data by release type
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns.boxplot(x= 'binge_release', y = 'imdb_score', data = df)
    ax.set_ylabel('IMDb Score')
    ax.set_xlabel('Release Type')
    plt.show()

#simple_box_plot()
