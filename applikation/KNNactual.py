from scipy.spatial.distance import euclidean


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
        self.addExtras() #tilføjer til sidst rating til koordinatsystemet.

    #Tilføjer rating til koordinatsystemet refinedGenres
    def addExtras(self):
        for film in self.filmListe: #Gå igennem alle film.
            film.refinedGenres['rating'] = film.rating / 10 


    def findAfstande(self):
        a = list(self.testFilm.refinedGenres.values())
        for film in self.filmListe:
            b = list(self.filmListe[1].refinedGenres.values())
            self.afstande.append(euclidean)

            

    



class Film:
    def __init__(self, name, genres, rating,kanLide):
        self.name = name #Filmens navn
        self.rawGenres = genres #liste over genrer denne film har.
        self.rawGenresDict = {} 
        self.refinedGenres = {} #dict over alle genrer vi har set, samt om denne film har dem
        self.rating = rating #Gennemsnitlig rating. Værdier fra 0,1 til 1.
        self.kanLide = kanLide # 1 = kan lide, -1 = kan ikke lide, 0 = testfilm.
           
         
    @staticmethod
    def genreDistance(movie1Genres,movie2Genres):
        return
