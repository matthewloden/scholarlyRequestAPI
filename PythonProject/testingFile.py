from scholarly import scholarly
import csv
# Retrieve the author's data, fill-in, and print
fieldnames = ['first_Name', 'last_Name', 'University','Blank', 'Citations']
#print(fieldnames)

search_query = scholarly.search_author('lori taylor, texas a&m university')
                
authors = scholarly.fill(next(search_query))

#authors['publications'][0]['bib']['title']
myvar = [0 for x in range(199)]
for i, publication in enumerate(authors['publications']):
    #print(publication['bib']['title'])
    if i < 199:
        myvar[i] = publication['bib']['title'].encode('utf-8').decode('ascii','ignore')

try: 
    with open('new_test_names.csv','w',newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(fieldnames)
        csv_writer.writerow(['lori','taylor','texas a&m university','']+myvar)
        
except:
    print("An error has occured with the print to the csv file")