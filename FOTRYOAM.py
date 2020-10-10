import imdb

a = imdb.IMDb()
movie = input('Enter Movie Name:')
search = a.search_movie(movie)
year = search[0]['year']
print(search[0]['title']+":"+str(year))
