import requests
from serpapi import GoogleSearch
import json
import csv

fieldnames = ['first_Name','last_Name','University','Blank','Citations']
authorNames = []
with open('Mk2SerpAPI/test_Names.csv' , mode = 'r') as testNames:
  csvreader = csv.DictReader(testNames,fieldnames=fieldnames)
  next(csvreader) #skips header
  for line in csvreader:
    authorNames.append(line['first_Name'] + ' ' + line['last_Name'] + ', ' + line['University'])

#have aquired author names and placed them in an array called authorNames

#time to send the api request
# for names in authorNames:
#   params = {
#     "engine": "google_scholar_profiles",
#     "mauthors": names,
#     #"api_key": "secret_api_key"    #need to store this in a secret way
#   }
#   print("Working On: ",params)
#   search = GoogleSearch(params)
#   results = search.get_dict()     #returns data in json format which will be of dictionary type
#   author = results['author']

with open('Mk2SerpAPI/authorID.json','r') as jsonFile:
  jsonObject = json.load(jsonFile)
  jsonFile.close()

author_id = jsonObject['profiles'][0]['author_id']
affiliations = jsonObject['profiles'][0]['affiliations']

print(author_id,' , ',affiliations)

