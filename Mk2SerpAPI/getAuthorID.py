import requests
from serpapi import GoogleSearch
import json
import pandas as pd

df = pd.read_csv('Mk2SerpAPI/test_Names.csv')

# print(df)
searchInput = []
for index, row in df.iterrows():
  searchInput.append(row['first_Name']+' '+row['last_Name']+', '+row['University'])
print(searchInput)
#have aquired author names and placed them in an array called searchInput

#time to send the api request
for names in searchInput:
  params = {
    "engine": "google_scholar_profiles",
    "mauthors": names,
    #"api_key": "secret_api_key"    #need to store this in a secret way
  }
  print("Working On: ",names)

  # search = GoogleSearch(params)
  # results = search.get_dict()
  # profiles = results['profiles']


##implementation with json object not found recursivly

with open('Mk2SerpAPI/authorID.json','r') as jsonFile:
  jsonObject = json.load(jsonFile)
  jsonFile.close()

author_id = jsonObject['profiles'][0]['author_id']
affiliations = jsonObject['profiles'][0]['affiliations']

kalenaID = "MMzxAS8AAAAJ"
kalenaAffiliation = "Texas A&M Univ, National Bureau of Economic Research (NBER), Institute for the Study of …"
robertID = "YQJOP48AAAAJ"
robertAffilliation = "Texas A&M University"

df['authorID'] = author_id,kalenaID,robertID
df['affiliation'] = affiliations,kalenaAffiliation,robertAffilliation


df.to_csv('Mk2SerpAPI/authorIDFile.csv')