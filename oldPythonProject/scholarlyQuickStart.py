from scholarly import scholarly

#print(next(scholarly.search_author('Lori L. Taylor')))

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Robert Greer, Texas A&M University')
authors = scholarly.fill(next(search_query))

#authors['publications'][0]['bib']['title']

for publication in authors['publications']:
    print(publication['bib']['title'])

#scholarly.pprint(author)
#for author in authors['publications'][0]:
#    for publication in author['bib']:
#        print(publication['title'])

# Print the titles of the author's publications
#print([pub['bib']['title'] for pub in author['publications']])

# Take a closer look at the first publication
#pub = scholarly.fill(author['publications'][0])
#print(pub)

# Which papers cited that publication?
#print([citation['bib']['title'] for citation in scholarly.citedby(pub)])