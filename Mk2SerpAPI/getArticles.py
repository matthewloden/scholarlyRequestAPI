from os import close
from serpapi import GoogleSearch
import json
import pandas as pd

mySecret = open("Mk2SerpAPI/secret.txt","r")
myAPIKey = mySecret.read()
mySecret.close()

df = pd.read_csv('Mk2SerpAPI/testAuthorIdOutput.csv')   #Reading Middle File, Change this to the file you are trying to run

authorID = []
for index, row in df.iterrows():
  authorID.append(row['author_id'])

output  = []


## Begin Looping through data

index = 0
for IDs in authorID:    
    params = {
    "engine": "google_scholar_author",
    "author_id": IDs,
    "api_key": myAPIKey
    }

    #if the data could not find an author id in the first part do this function
    if IDs == "Google hasn't returned any results for this query.":
      print("Google hasn't returned any results for: ",df['name'][index],', completed ',index,' out of ',len(df['name']))##working with people that don't have any data
      df4 = pd.DataFrame({
        'university' : df['university'][index],
        'name' : df['name'][index],
        'projectid' : df['projectid'][index],
        'author_id' : IDs,
        'affiliations' : df['affiliations'][index],
        'Article Title' : "No Author ID Found",
        'Article Publication' : 'No Author ID Found',
        'Year of Citation' : 'No Author ID Found',
        'Number of Citations that Year' : 'No Author ID Found'
      },
      index=[1]
      )
      output.append(df4)
    
    
    #if we could find data on the author id sending api request
    else:
      search = GoogleSearch(params)
      data = search.get_dict() 
      
      if data["search_metadata"]["status"] == "Success":    #if the api responds with information about the person we looked up
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
          df3['name'] = data['author']['name']
          df3['affiliations'] = data['author']['affiliations']
          df3['university'] = df['university'][index]
          df3['projectid'] = df['projectid'][index]
        else:
          df2['author_id'] = IDs
          df2['name'] = data['author']['name']
          df2['affiliations'] = data['author']['affiliations']
          df2['university'] = df['university'][index]
          df2['projectid'] = df['projectid'][index]

        # print(df3)
        
        result =  pd.concat([df2,df3],axis=1)
        # print(result)
        output.append(result)


      else:       ##if the api request does not correctly return or fails
        print("Failure Getting data from: ",data["author"]["name"],' ,',IDs)
        df4 = pd.DataFrame({
        'university' : df['university'][index],
        'name' : df['name'][index],
        'projectid' : df['projectid'][index],
        'author_id' : IDs,
        'affiliations' : df['affiliations'][index],
        'Article Title' : "No Author ID Found",
        'Article Publication' : 'No Author ID Found',
        'Year of Citation' : 'No Author ID Found',
        'Number of Citations that Year' : 'No Author ID Found'
        },
        index=[1]
        )
        output.append(df4)
    
      # output.append(df4)
    index = index + 1

    
    
# print(output)
trueOutput = pd.concat(output)
# print(trueOutput)
cols = list(trueOutput.columns.values)
print(cols)
trueOutput = trueOutput[['university','name','projectid','author_id','affiliations','Article Title','Article Publication','Year of Citation','Number of Citations that Year']]
print(trueOutput)
trueOutput.to_csv('Mk2SerpAPI/partialOutputDataVersion1.csv')