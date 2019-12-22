import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import data_frame_creation

df_list = data_frame_creation.create_TV_data_frames()
df = df_list[0]
df_first_10[1]
first_10_binge[2]
first_10_serial[3]
#initial code in place to call the dataframe creation function and get the set of dataframes we need

def pair_plot_attempt():
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns.pairplot(df_first_10 , x_vars=['episode'], y_vars=['imdb_score'], hue='binge_release')
    plt.show()

#pair_plot_attempt()

#episode_stack_plot()

def dual_hist_plot(df_1, df_2):
    #takes in two dataframes and returns a dual histogram of both layered
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    hist_serial = sns.distplot(df_1['imdb_score'], kde = False)
    hist_binge = sns.distplot(first_10_binge['imdb_score'], kde = False)
    fig.legend(labels=['Serial','Batch'])
    hist_serial.set_xlabel('IMDb Score')
    plt.show()

def heat_map():
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    corr = first_10_binge.corr()
    corr = corr.drop(['moviedb_votes', 'moviedb_score'], axis=1)
    corr = corr.drop(['moviedb_votes', 'moviedb_score'], axis=0)
    print(corr.head)
    ax = sns.heatmap(corr, square = True)
    plt.show()

#heat_map()
hist_plot()

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

def simple_box_plot():
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns.boxplot(x= 'binge_release', y = 'imdb_score', data = df)
    ax.set_ylabel('IMDb Score')
    ax.set_xlabel('Release Type')
    plt.show()

#simple_box_plot()

def stack_plot():
    plt.style.use('seaborn')
    fig = plt.figure()
    sns.set_palette('colorblind')
    ax = df.plot.area()
    plt.show()

#stack_plot()
