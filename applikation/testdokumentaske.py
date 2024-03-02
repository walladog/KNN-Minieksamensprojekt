#Denne fil er lavet til at teste om KNNactual fungerer ordentligt.

from KNNactual import *
from BetterMovieDB_API import *
import numpy as np
from scipy.spatial.distance import euclidean

response = findFilm('forrest gump')
response2 = findFilm('toy story')
test1 = findFilm("the boy and the heron")

#print(response)

filmgøj = FilmListeKlasse()

filmgøj.addFilm(response['original_title'],response['genre_ids'],response['vote_average'],-1)
filmgøj.addFilm(response2['original_title'],response2['genre_ids'],response2['vote_average'],-1)

filmgøj.addFilm(test1['original_title'],test1['genre_ids'],test1['vote_average'],0,True)


filmgøj.generateRefinedGenres()
#print(filmgøj.filmListe[0].refinedGenres)

a = list(filmgøj.filmListe[0].refinedGenres.values())
b = list(filmgøj.filmListe[1].refinedGenres.values())
gumpgenrer = filmgøj.filmListe[0].rawGenres
print(list(filmgøj.testFilm.refinedGenres.values()))
print(a)
#print(filmgøj.filmListe[1].rawGenres)


# print(filmgøj.filmListe[1].refinedGenres)
#print(filmgøj.genreDict)





filmgøj.findAfstande()
print(filmgøj.filmListe[0].afstandFraTest)
print(filmgøj.filmListe[1].afstandFraTest)






svar = filmgøj.KNN(1)
print(filmgøj.filmListe[0].afstandFraTest)
print(filmgøj.filmListe[1].afstandFraTest)
print(filmgøj.filmListe[0].name)
print(svar)