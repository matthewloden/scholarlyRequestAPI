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
  if row['university'] == "360222-UMCP":
    searchInput.append(row['name']+', University of Maryland')  
  else:
    searchInput.append(row['name']+', '+row['university'])
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
  try:
    profiles = results['profiles']
    # print(profiles)
    try:
      author_id.append(profiles[0]['author_id'])
    except KeyError:
      author_id.append('ERROR Getting Author ID')
    try:
      affiliations.append(profiles[0]['affiliations'])  
    except KeyError:
      affiliations.append('ERROR Getting Affiliation')
  except KeyError:
    author_id.append(results['error'])
    affiliations.append(results['error'])
    

  

df['author_id'] = author_id
df['affiliations'] = affiliations

print(df)

df.to_csv('Mk2SerpAPI/testAuthorIdOutput.csv')