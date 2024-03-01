#Denne fil er lavet til at teste om KNNactual fungerer ordentligt.

from KNNactual import *
from BetterMovieDB_API import *
import numpy as np
import scipy.spatial.distance as dist

response = findFilm('forrest gump')
response2 = findFilm('toy story')

#print(response)

filmgøj = FilmListeKlasse()

filmgøj.addFilm(response['original_title'],response['genre_ids'],response['vote_average'],response['vote_count'])
filmgøj.addFilm(response2['original_title'],response2['genre_ids'],response2['vote_average'],response2['vote_count'])


filmgøj.generateRefinedGenres()
#print(filmgøj.filmListe[0].refinedGenres)

a = list(filmgøj.filmListe[0].refinedGenres.values())
b = list(filmgøj.filmListe[1].refinedGenres.values())
gumpgenrer = filmgøj.filmListe[0].rawGenres
print(gumpgenrer)
print(filmgøj.filmListe[1].rawGenres)

print((a))
print((b))
print(filmgøj.genreDict)
# print(filmgøj.filmListe[1].refinedGenres)
#print(filmgøj.genreDict)

# print(np.sum([a,b]))

print(dist.euclidean(a,b))