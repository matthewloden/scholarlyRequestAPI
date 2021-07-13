import requests
# from serpapi import GoogleSearch
import json
import csv

with open('test_Names.csv',mode = 'r') as testNames:
  csvreader = csv.reader(testNames)
  for line in csvreader:
    myVar = line

print(myVar)

params = {
  "engine": "google_scholar_profiles",
  "mauthors": "Lori Taylor",
  #"api_key": "secret_api_key"
}

# search = GoogleSearch(params)
# results = search.get_dict()
# author = results['author']

print(params)