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
    # print (data)
    
    if data["search_metadata"]["status"] == "Success":
      print("Success on Getting Information from: ",data["author"]["name"],' ,',IDs)
      articlesTitle = []
      articlesPublication = []
      articlesYearpub = []
      articlesNumYearPub = []
      for item in data["articles"]:
        articlesTitle.append(item["title"])
        articlesPublication.append(item["publication"])
      # print (articlesTitle)
      for line in data["cited_by"]["graph"]:
        articlesYearpub.append(line["year"])
        articlesNumYearPub.append(line["citations"])

      df2 = pd.DataFrame(articlesTitle,columns=['Article Title'])
      df2['Article Publication'] = articlesPublication
      df2['authorID'] = IDs
      # print(df2)
      df3 = pd.DataFrame(articlesYearpub,columns=['Year of Publication'])
      # df2['Year of Publication'] = pd.Series(articlesYearpub)
      df3['Number of Publications that Year'] = articlesNumYearPub   #the series might break the code once were working with the full data set
      df3['authorID'] = IDs
      # print(df3)
      


    if data["search_metadata"]["status"] == "Failure":
      print("Failure Getting data from: ",data["author"]["name"],' ,',IDs)

print(df)

frames =  [df,df2,df3]

result =  pd.concat(frames,axis=1,join="outer")
print(result)
result.to_csv('Mk2SerpAPI/outputData.csv')
# df2.to_csv('Mk2SerpAPI/outputData2.csv')