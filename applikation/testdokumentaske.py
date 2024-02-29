#Denne fil er lavet til at teste om KNNactual fungerer ordentligt.

from KNNactual import *
from BetterMovieDB_API import *

response = findFilm('toy story 2')
response2 = findFilm('toy story')

filmgøj = FilmListeKlasse()

filmgøj.addFilm(response['original_title'],response['genre_ids'],response['vote_average'],response['vote_count'])
filmgøj.addFilm(response2['original_title'],response2['genre_ids'],response2['vote_average'],response2['vote_count'])

filmgøj.generateRefinedGenres()
print(filmgøj.filmListe[1].refinedGenres)