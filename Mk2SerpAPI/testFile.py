from pandas.core.frame import DataFrame
import requests
from serpapi import GoogleSearch
import json
import pandas as pd

mySecret = open("Mk2SerpAPI/secret.txt","r")
myAPIKey = mySecret.read()
mySecret.close()


params = {
    "engine": "google_scholar_profiles",
    "mauthors": "Michael Cobb, North Carolina State Universtiy",
    "api_key": myAPIKey  
  }
print("Working On: ","Michael Cobb")

search = GoogleSearch(params)
results = search.get_dict()
print(results)

print(results['profiles'])

print(results['error'])