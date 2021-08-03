from os import close
from serpapi import GoogleSearch
import json
import pandas as pd

mySecret = open("Mk2SerpAPI/secret.txt","r")
myAPIKey = mySecret.read()
mySecret.close()

df = pd.read_csv('Mk2SerpAPI/authorIDFile.csv')

authorID = []
for index, row in df.iterrows():
  authorID.append(row['author_id'])
  numAuthors = index
#print(authorID)
index = index + 1
# print(index)
output  = []


## Begin Looping through data


for IDs in authorID:    
    params = {
    "engine": "google_scholar_author",
    "author_id": IDs,
    "api_key": myAPIKey
    }
    search = GoogleSearch(params)
    data = search.get_dict() 
    
    if data["search_metadata"]["status"] == "Success":
      print("Success on Getting Information from: ",data["author"]["name"],' ,',IDs)
      articlesTitle = []
      articlesPublication = []
      articlesYearpub = []
      articlesNumYearPub = []
      for item in data["articles"]:
        try:
          articlesTitle.append(item["title"])
          # print(item['title'])
        except KeyError:
          articlesTitle.append('No Title Found, ERROR')
          # print('Missing Title in ',IDs)
        try:
          articlesPublication.append(item["publication"])
        except KeyError:
          articlesPublication.append('No Publication Found, ERROR')
      # print (articlesTitle)
      for line in data["cited_by"]["graph"]:
        try:
          articlesYearpub.append(line["year"])
          articlesNumYearPub.append(line["citations"])
        except KeyError:
          articlesYearpub.append("No Records Found")
          articlesNumYearPub.append("No Records Found")

      df2 = pd.DataFrame(articlesTitle,columns=['Article Title'])
      df2['Article Publication'] = articlesPublication
      # print(df2)
      df3 = pd.DataFrame(articlesYearpub,columns=['Year of Citation'])
      # df2['Year of Publication'] = pd.Series(articlesYearpub)
      df3['Number of Citations that Year'] = articlesNumYearPub 

      if len(data['articles']) < len(data['cited_by']['graph']):
        df3['author_id'] = IDs
        df3['Name'] = data['author']['name']
        df3['Affiliation'] = data['author']['affiliations']
      else:
        df2['author_id'] = IDs
        df2['Name'] = data['author']['name']
        df2['Affiliation'] = data['author']['affiliations']
      

      # print(df3)
      
      result =  pd.concat([df2,df3],axis=1)
      # print(result)
      output.append(result)


    else:
      print("Failure Getting data from: ",data["author"]["name"],' ,',IDs)
      df4 = {
        "Name" : [],
        "affiliation" : [],
        "author_id" : [IDs],
        "Article Title" : ["ERROR"],
        "Article Publication" : ["ERROR"],
        "Year of Citation" : ["ERROR"],
        "Number of Citations that Year" : ["ERROR"]
      }
      output.append(df4)

# print(output)
trueOutput = pd.concat(output)
# print(trueOutput)
cols = list(trueOutput.columns.values)
print(cols)
trueOutput = trueOutput[['Name','Affiliation','author_id','Article Title','Article Publication','Year of Citation','Number of Citations that Year']]
print(trueOutput)
trueOutput.to_csv('Mk2SerpAPI/outputData.csv')