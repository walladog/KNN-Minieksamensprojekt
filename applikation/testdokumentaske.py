#Denne fil er lavet til at teste om KNNactual fungerer ordentligt.

from KNNactual import *
from BetterMovieDB_API import *
import numpy as np
from scipy.spatial.distance import euclidean

response = findFilm('forrest gump')
response2 = findFilm('toy story')
r3 = findFilm('cock fight')
r4 = findFilm('revenge of the sith')
r5 = findFilm('the big lebowski')


test1 = findFilm("the boy and the heron")

#print(response)

filmgøj = FilmListeKlasse()

filmgøj.addFilm(response['original_title'],response['genre_ids'],response['vote_average'],-1)
filmgøj.addFilm(response2['original_title'],response2['genre_ids'],response2['vote_average'],-1)
filmgøj.addFilm(r3['original_title'],r3['genre_ids'],r3['vote_average'],1)
filmgøj.addFilm(r4['original_title'],r4['genre_ids'],r4['vote_average'],-1)
filmgøj.addFilm(r5['original_title'],r5['genre_ids'],r5['vote_average'],1)

filmgøj.addFilm(test1['original_title'],test1['genre_ids'],test1['vote_average'],0,True)


filmgøj.generateRefinedGenres()






svar = filmgøj.KNN(5)

for i in range(5):
    print(f"{filmgøj.filmListe[i].afstandFraTest} + {filmgøj.filmListe[i].name}")




print(svar)