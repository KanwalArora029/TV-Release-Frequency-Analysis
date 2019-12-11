import json
import requests
import mysql.connector
import omdb

#import config
api_key = "d04df101"

omdb.set_default('apikey', api_key)

response  = omdb.request(t = 'Stranger Things')
print(response)
data = response.json()

print(data)

#This works but you must pass it a title or a year, it cannot just accept a year
