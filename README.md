# TV-Release-Frequency-Analysis

In general this project was meant to serve as an intro into data gathering through API calls and web scraping as well as MySQL database management.

The purpose of this specific analysis is to determine if there is a significant difference in IMDb ratings and vote counts for TV shows that were released in a 'batch' vs shows that are released in more traditional serialized format. 


Data for this project will be gather from two main sources.
1. The Movie DB API.
    A.) I used their TV show discover API to select all new shows that have been released in the 2019 calendar year. A table           was created to hold show information and another one to hold episode level information. This ended up being a rather           large data set contain around 30,000 episodes of TV
    B.) Then their external IDs API was used to match each show with their IMDb id. Note that this was only done with shows           that have 5 or more votes on the Movie DB API
    
2. Webscraping IMDb show pages.
    A.) Using Beautiful Soup in conjunction with each shows IMDb ID. I scraped each season 1 show page to get IMDb ratings and         vote counts for each individual episode.
