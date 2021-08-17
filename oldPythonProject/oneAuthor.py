from scholarly import scholarly
import csv

###############################################################################################################################################################################
###############################################################################################################################################################################
##############  Opening CSV File called test_Names
###############################################################################################################################################################################
###############################################################################################################################################################################
myvar = [None]*4
with open('test_Names.csv', mode = 'r') as test_Names:
    csv_reader = csv.reader(test_Names)
    for i,line in enumerate(csv_reader):
        myvar[i] = line

#print(myvar[1][0])
myRequest = [None]*4
for j in range(4):
    myRequest[j] = myvar[j][0] + ' ' + myvar[j][1] + ', ' + myvar[j][2]
#print(myRequest)
myResult = [None]*150
fieldnames = myvar[0]
myRequest.pop(0)
myOutput = [None]*4
myvar.pop(0)
k = 0
for item in myRequest:
    print("Working on: ",item)
    searchQuery = scholarly.search_author(item)
    authors = scholarly.fill(next(searchQuery))

    for i, publication in enumerate(authors['publications']):
        #print(publication['bib']['title'])
        if i < 149:
            myResult[i] = publication['bib']['title'].encode('utf-8').decode('ascii','ignore')
    
    myOutput[k] = myvar[k]+myResult
    print(myOutput[k])
    k = k + 1
#print(myResult)

#try:
with open('newNames.csv','w',newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    csv_writer.writerow(fieldnames)
    #for row in myOutput:
    csv_writer.writerow(myOutput)
# except:
#     print("An error has occured within the print to csv function")

# for i, line in enumerate(csv_reader): 
#         if(i > 0):
#             myRequest = line['first_Name'] + " " + line['last_Name'] + ", " + line['University']
#             search_query = scholarly.search_author(myRequest)
            
#             authors = scholarly.fill(next(search_query))

#             #authors['publications'][0]['bib']['title']

#             for i, publication in enumerate(authors['publications']):
#                 print(publication['bib']['title'])
#                 #line[i + 5] = publication['bib']['title']
                    
            
        
# ###############################################################################################################################################################################
# ###############################################################################################################################################################################
# ##############  Writing to CSV File called new_Names
# ###############################################################################################################################################################################
# ###############################################################################################################################################################################
# try:
#     with open('new_Names.csv', mode = 'w') as new_Names:
#         csv_writer = csv.writer(new_Names)
# except:
#     print("An error has occured within the print to csv function")
        


        