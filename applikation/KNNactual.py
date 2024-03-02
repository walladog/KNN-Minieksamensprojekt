from scipy.spatial.distance import euclidean


class FilmListeKlasse:
    def __init__(self):
        self.genreDict = {}
        self.filmListe = []
        self.testFilm = None
        self.afstande = []

    def addFilm(self,name,genres,rating,kanLide):
        self.filmListe.append(Film(name,genres,rating,kanLide))
        self.addGenresToGenreDict(self.filmListe[-1])


    def addGenresToGenreDict(self,film):
        for genre_id in film.rawGenres:
            if str(genre_id) in self.genreDict.keys():
                pass
            else:
                self.genreDict[str(genre_id)] = 0
    
    def generateRefinedGenres(self):
        for genre in self.genreDict.keys():
            for film in self.filmListe:
                if int(genre) in film.rawGenres:
                    film.refinedGenres[genre] = 1
                else:
                    film.refinedGenres[genre] = 0
        #self.addExtras() #tilføjer rating til koordinatsystemet.

    def addExtras(self):
        for film in self.filmListe:
            film.refinedGenres['rating'] = film.rating / 10

    def nyTestFilm(self,name, genres, rating):
        self.testFilm = Film(name,genres,rating,0)
        self.addGenresToGenreDict(self.testFilm)

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
        self.rating = rating
        self.kanLide = kanLide # 1 = kan lide, -1 = kan ikke lide, 0 = test
           
         
    @staticmethod
    def genreDistance(movie1Genres,movie2Genres):
        return
