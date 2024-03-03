from scipy.spatial.distance import euclidean

# Tutorial til at bruge denne fil.
# Et eksempel på korrekt brug af denne film kan ses i filen 'testdokumentaske.py'
# Lav et FilmListeKlasse-objekt.
# brug metoden addFilm() sammen med responsen fra dit API-kald til at tilføje film og deres bedømmelser.
# brug igen metoden addFilm() til at tilføje en testfilm (husk at sætte kanLide = 0 og test = True)
# Kald metoden generateRefinedGenres().
# Kald metoden KNN() med et ulige tal som input. outputtet vil være enten 1 eller -1, om algoritmen tror brugeren kan lide filmen eller ej.


class FilmListeKlasse:
    def __init__(self):
        self.genreDict = {} #keysne er genre_id for alle de genrer, der er set indtil videre. values er alle 0.
        self.filmListe = [] #Liste over film-objekter
        self.testFilm = None #Den film, der skal vurderes.
        self.afstande = [] #filmene i filmlistes afstande fra testfilm.

    #Tilføjer et film-objekt til filmListe.
    def addFilm(self,name,genres,rating,kanLide,test = False):
        if test: #Eksekveres hvis dette er en testfilm.
            self.testFilm = Film(name,genres,rating,0)
            if self.addGenresToGenreDict(self.testFilm): #Tjek om der er nye genrer og tilføj dem.
                self.generateRefinedGenres() #Hvis der er nye genrer skal de også tilføjes til alle de andre films refinedGenres-dicts.
        else: #Eksekveres hvis dette ikke er en testfilm.
            self.filmListe.append(Film(name,genres,rating,kanLide))
            self.addGenresToGenreDict(self.filmListe[-1])

    #Tjekker om en film indeholder genrer, som ikke allerede er i hovedlisten genreDict.
    #Hvis en genre ikke er i genreDict, tilføjes den.
    #Returner True hvis filmen indeholder en ny genre, ellers returner False.
    def addGenresToGenreDict(self,film):
        erDerNyeGenrer = False
        for genre_id in film.rawGenres:
            if str(genre_id) in self.genreDict.keys():
                pass
            else:
                self.genreDict[str(genre_id)] = 0
                erDerNyeGenrer = True
        return erDerNyeGenrer
    

    # Køres når brugeren er færdig med at bedømme film.
    # Køres også når en testfilm indeholder en hidtil uset genre.
    def generateRefinedGenres(self):
        for genre in self.genreDict.keys(): #Vi går alle keys (genre_ids) igennem.
            for film in self.filmListe: #For hver genre går vi alle film i filmListe igennem
                if int(genre) in film.rawGenres: #Tjek om genren er i filmens rå genreliste. Tilføj den til filmens refinedGenres dict.
                    film.refinedGenres[genre] = 1
                else:
                    film.refinedGenres[genre] = 0
        
        #Hvis der er en testfilm, skal dens genreliste også gennemgås.
        if self.testFilm != None:
            for genre in self.genreDict.keys():
                if int(genre) in self.testFilm.rawGenres:
                    self.testFilm.refinedGenres[genre] = 1
                else:
                    self.testFilm.refinedGenres[genre] = 0

        self.addExtras() #tilføjer til sidst rating til koordinatsystemet.

    #Tilføjer rating til koordinatsystemet refinedGenres
    def addExtras(self):
        for film in self.filmListe: #Gå igennem alle film.
            film.refinedGenres['rating'] = film.rating / 10 
        if self.testFilm != None:
            self.testFilm.refinedGenres['rating'] = self.testFilm.rating / 10

    #Finde hver film i filmListes afstand fra testfilmen og sætter deres attribut afstandFraTest lig resultatet.
    #Kaldes i metoden KNN()
    def findAfstande(self):
        testPunkt = list(self.testFilm.refinedGenres.values())
        for film in self.filmListe:
            b = list(film.refinedGenres.values())
            film.afstandFraTest = (euclidean(testPunkt,b))

    #Sorterer filmListe fra korteste afstand fra testpunktet til længste vha. selection sort.
    #Kaldes i metoden KNN()
    def sorterfilmListe(self):
        for i in range(0,len(self.filmListe)-1):
            min = i
            for j in range(i+1 , len(self.filmListe)):
                if self.filmListe[j].afstandFraTest < self.filmListe[min].afstandFraTest:
                    min = j        
            (self.filmListe[i] , self.filmListe[min]) = ( self.filmListe[min] , self.filmListe[i]) 
    
    #find testfilmens k nærmeste naboer samt om brugeren har bedømt dem positivt/negativt. Bedøm derefter denne film.
    def KNN(self,k):
        if k % 2 == 0: 
            print("k skal være et ulige tal")
            return
        elif len(self.filmListe) < k:
            print("k må ikke være større end antallet af film, du har bedømt.")
            return
        elif len(self.filmListe) == 0:
            print("Du skal bedømme mindst 1 film først.")
            return
        
        #Afstandene findes og sorteres.
        self.findAfstande()
        self.sorterfilmListe()
        forudsigelse = 0

        for i in range(k):
            forudsigelse += self.filmListe[i].kanLide

        forudsigelse = forudsigelse / abs(forudsigelse) #Normaliser til 1 eller -1
        return forudsigelse

        
        


#Denne her klasse er stort set bare en container for en masse attributter.
class Film:
    def __init__(self, name, genres, rating,kanLide):
        self.name = name #Filmens navn
        self.rawGenres = genres #liste over genrer denne film har.
        self.refinedGenres = {} #dict over alle genrer vi har set, samt om denne film har dem
        self.rating = rating #Gennemsnitlig rating. Værdier fra 0,1 til 1.
        self.kanLide = kanLide # 1 = kan lide, -1 = kan ikke lide, 0 = testfilm.
        self.afstandFraTest = None #Afstanden til testfilmen.
           

