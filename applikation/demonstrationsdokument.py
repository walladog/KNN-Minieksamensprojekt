#Denne fil er lavet til at simulere de funktions- og metodekald, som ville ske hvis en bruger brugte vores side.

#Hjemmesiden loader op, og diverse dependencies initialiseres sammen med et FilmListeKlasse-objekt
from KNNactual import *
from BetterMovieDB_API import *
import numpy as np
from scipy.spatial.distance import euclidean
filmListe = FilmListeKlasse()

#Brugeren søger på filmen Forrest gump, og trykker på knappen 'kan ikke lide'
r1 = findFilm('forrest gump')
filmListe.addFilm(r1['original_title'],r1['genre_ids'],r1['vote_average'],-1)

#Brugeren gentager processen 4 gange mere.
r2 = findFilm('toy story')
filmListe.addFilm(r2['original_title'],r2['genre_ids'],r2['vote_average'],-1)

r3 = findFilm('cock fight')
filmListe.addFilm(r3['original_title'],r3['genre_ids'],r3['vote_average'],1)

r4 = findFilm('revenge of the sith')
filmListe.addFilm(r4['original_title'],r4['genre_ids'],r4['vote_average'],1)

r5 = findFilm('the big lebowski')
filmListe.addFilm(r5['original_title'],r5['genre_ids'],r5['vote_average'],-1)

#Brugeren trykker på knappen 'evaluer', og det er nu programmets tur til at gætte, om brugeren kan lide en given film.
#Brugeren søger på filmen 'the boy and the heron.'
test1 = findFilm("the boy and the heron")
filmListe.addFilm(test1['original_title'],test1['genre_ids'],test1['vote_average'],0,True)
filmListe.generateRefinedGenres()

#KNN-algoritmen køres med en valgt k-værdi.
svar = filmListe.KNN(3)

print(svar)