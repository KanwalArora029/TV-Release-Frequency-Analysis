import requests
from bs4 import BeautifulSoup
import mysql_etl_functions

def google_news_scraper():

    show_list = mysql_etl_functions.get_show_name()
    i = 0
    for show in show_list:
        print(show[0])
        show_name = show[0].replace(' ', '%20')
        print(show_name)
        url = 'https://news.google.com/search?q='+ show_name +'when%3A1y&hl=en-US&gl=US&ceid=US%3Aen'
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        list = soup.find_all(class_="WW6dff uQIVzc Sksgp")
        print(list[0])
        print(len(list))
        i += 1
        if i == 10:
            return


google_news_scraper()
