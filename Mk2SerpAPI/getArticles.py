from serpapi import GoogleSearch
import json
import pandas as pd

df = pd.read_csv('Mk2SerpAPI/authorIDFile.csv')

authorID = []
for index, row in df.iterrows():
  authorID.append(row['authorID'])
#print(authorID)

for IDs in authorID:    
    params = {
    "engine": "google_scholar_author",
    "author_id": IDs,
    "api_key": "secret_api_key"
    }
    #print(params)
    # search = GoogleSearch(params)
    # results = search.get_dict() 
    with open("Mk2SerpAPI/testArticles.json") as testFile:
      data = json.load(testFile)
      testFile.close()
    print (data)
    
    if data["search_metadata"]["status"] == "Success":
      print("Error getting information on: ",IDs)

    


print(df)