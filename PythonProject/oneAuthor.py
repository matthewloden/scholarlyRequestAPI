from scholarly import scholarly
import csv

#search_query = scholarly.search_author('Lori Taylor')
#scholarly.pprint(next(search_query))
###############################################################################################################################################################################
###############################################################################################################################################################################
##############  Opening CSV File called test_Names
###############################################################################################################################################################################
###############################################################################################################################################################################

with open('test_Names.csv', mode = 'r') as test_Names:
    fieldnames = ['first_Name', 'last_Name', 'University','Blank', 'Citations']
    csv_reader = csv.DictReader(test_Names, fieldnames=fieldnames, delimiter = ',')
    csv_reader = list(csv_reader)
    for i, line in enumerate(csv_reader): 
            if(i > 0):
                myRequest = line['first_Name'] + " " + line['last_Name'] + ", " + line['University']
                search_query = scholarly.search_author(myRequest)
                
                authors = scholarly.fill(next(search_query))

                #authors['publications'][0]['bib']['title']

                for i, publication in enumerate(authors['publications']):
                    #print(publication['bib']['title'])
                    line[i + 5] = publication['bib']['title']
                    
                
            
    
    ###############################################################################################################################################################################
    ###############################################################################################################################################################################
    ##############  Writing to CSV File called new_Names
    ###############################################################################################################################################################################
    ###############################################################################################################################################################################

    with open('new_Names.csv', mode = 'w') as new_Names:
        fieldnames = ['first_Name', 'last_Name', 'University','Blank', 'Citations']
        for i in range(177):
            fieldnames.append(i)
        csv_writer = csv.DictWriter(new_Names,fieldnames=fieldnames, delimiter = ',', extrasaction='raise')

        for line in csv_reader:
            print(line)
            csv_writer.writerow(line)
        


        