import tmdbsimple as tmdb

tmdb.API_KEY = 'eff920c443abd1666a0f18cb478d18a7'
search = tmdb.Search()
response = search.movie(query='The Bourne')
for s in search.results:
    print(s['title'], s['release_date'])

#http://www.omdbapi.com/?t=the%20pink%20panther&y=&plot=short&r=xml
    
