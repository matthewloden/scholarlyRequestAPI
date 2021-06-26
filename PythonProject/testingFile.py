from scholarly import scholarly
import csv
# Retrieve the author's data, fill-in, and print
fieldnames = ['first_Name', 'last_Name', 'University','Blank', 'Citations']
for i in range(177):
    fieldnames.append(i)
#print(fieldnames)

search_query = scholarly.search_author('lori taylor, texas a&m university')
                
authors = scholarly.fill(next(search_query))

#authors['publications'][0]['bib']['title']
myvar = [0 for x in range(177)]
for i, publication in enumerate(authors['publications']):
    #print(publication['bib']['title'])
    myvar[i] = publication['bib']['title']

#print(myvar)
listToStr = ', '.join([str(elem) for elem in myvar])    

print(listToStr)
try: 
    with open('new_test_names.csv','w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fieldnames)
        csv_writer.writerow(['lori','taylor','texas a&m university','',listToStr])

except:
    print("An error has occured with the print to the csv file")