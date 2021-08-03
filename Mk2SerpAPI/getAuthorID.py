from pandas.core.frame import DataFrame
import requests
from serpapi import GoogleSearch
import json
import pandas as pd

mySecret = open("Mk2SerpAPI/secret.txt","r")
myAPIKey = mySecret.read()
mySecret.close()

df = pd.read_csv('Mk2SerpAPI/test_Names.csv')

# print(df)
searchInput = []
for index, row in df.iterrows():
  searchInput.append(row['first_Name']+' '+row['last_Name']+', '+row['University'])
print(searchInput)
#have aquired author names and placed them in an array called searchInput

author_id = []
affiliations = []

#time to send the api request
for names in searchInput:
  params = {
    "engine": "google_scholar_profiles",
    "mauthors": names,
    "api_key": myAPIKey  
  }
  print("Working On: ",names)

  search = GoogleSearch(params)
  results = search.get_dict()
  profiles = results['profiles']

  # print(profiles)
  if profiles[0]['author_id']:
    author_id.append(profiles[0]['author_id'])
  else:
    author_id.append('ERROR')
  if profiles[0]['affiliations']:
    affiliations.append(profiles[0]['affiliations'])  
  else:
    affiliations.append('ERROR')

df['author_id'] = author_id
df['affiliations'] = affiliations

print(df)

df.to_csv('Mk2SerpAPI/authorIDFile.csv')