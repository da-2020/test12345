import pandas as pd
from pandas import DataFrame
import requests


# I used this line to upload the .csv into the notebook.
# df = pd.read_csv('C:/Work/Capstone/Project/latlon1.csv')


# import csv
df = pd.read_csv('latlon1.csv')

# dataframe contains one pair of lat/lon and placeholder variable to demonstrate for loop
print(df)

# convert dataframe columns to lists
latv = df['lat'].tolist()
lonv = df['lon'].tolist()

# variables are defined as before or with a "1" placeholder variable
search_query='chickfila'
radius=60000
LIMIT=500
CLIENT_ID = 1
CLIENT_SECRET = 1
ACCESS_TOKEN = 1
VERSION = 1

# create empty list to store iterated urls
urlcontainer = []

# setup "for" loop, pass in lists of latitude and longitude values
for i, j in set(zip(latv, lonv)):

    url='https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&oauth_token={}&v={}&query={}&radius={}&limit={}'.format(CLIENT_ID,
                                                                                                                                                CLIENT_SECRET,
                                                                                                                                                i,j, ACCESS_TOKEN,VERSION,
                                                                                                                                                search_query,radius,LIMIT)
    
    # add each modified url to list
    urlcontainer.append(url)


# create empty list to store results?
resultslist = []

# create another "for" loop to pass in our modified urls from "urlcontainer"
for x in urlcontainer:
    results = requests.get(x).json()
    # add results from api request to "resultslist" 
    resultslist.append(results)
    


# show results for diagostics
print(resultslist)

# convert list into dataframe? without API key, I only get garbage data and cannot be sure if this is the best way 
# to store final results
df1 = DataFrame(resultslist,columns=['results'])

print(df1)