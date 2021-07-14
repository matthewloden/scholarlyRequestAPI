import requests
from serpapi import GoogleSearch
import json
import csv

fieldnames = ['first_Name','last_Name','University','Blank','Citations']
authorNames = []
outputLine = []
with open('Mk2SerpAPI/test_Names.csv' , mode = 'r') as testNames:
  csvreader = csv.DictReader(testNames,fieldnames=fieldnames)
  next(csvreader) #skips header
  for line in csvreader:
    authorNames.append(line['first_Name'] + ' ' + line['last_Name'] + ', ' + line['University'])
    inputFirstName = line['first_Name']
    inputLastName = line['last_Name']
    inputUniversity = line['University']
    outputLine.append("{},{},{},{},{}\n".format(inputFirstName,inputLastName,inputUniversity,"authorid","affiliation")) 

print(outputLine)
#have aquired author names and placed them in an array called authorNames

#time to send the api request
# for names in authorNames:
#   params = {
#     "engine": "google_scholar_profiles",
#     "mauthors": names,
#     #"api_key": "secret_api_key"    #need to store this in a secret way
#   }
#   print("Working On: ",names)

# search = GoogleSearch.new(params)
# profiles = search.get_hash[:profiles]

with open('Mk2SerpAPI/authorID.json','r') as jsonFile:
  jsonObject = json.load(jsonFile)
  jsonFile.close()

author_id = jsonObject['profiles'][0]['author_id']
affiliations = jsonObject['profiles'][0]['affiliations']

kalenaID = "MMzxAS8AAAAJ"
kalenaAffiliation = "Texas A&M Univ, National Bureau of Economic Research (NBER), Institute for the Study of …"
robertID = "YQJOP48AAAAJ"
robertAffilliation = "Texas A&M University"

# outputLine.append("{},{}\n".format(author_id,affiliations))
# # # outputLine[1] += '\n'
# # # outputLine[2] += '\n'
# print(outputLine)

# with open('Mk2SerpAPI/authorIdFile.csv','w') as outputFile:
#   csvwriter = csv.writer(outputFile,delimiter = ',')
#   csvwriter.writerow(['first_Name','last_Name','University','AuthorID','Affiliation'])
  
