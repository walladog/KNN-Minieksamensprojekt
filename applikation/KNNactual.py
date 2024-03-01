
class FilmListeKlasse:
    def __init__(self):
        self.genreDict = {}
        self.filmListe = []

    def addFilm(self,name,genres,rating,popularity):
        self.filmListe.append(Film(name,genres,rating,popularity))
        self.addGenresToGenreDict(self.filmListe[-1])


    def addGenresToGenreDict(self,film):
        for genre_id in film.rawGenres:
            if str(genre_id) in self.genreDict.keys():
                pass
            else:
                self.genreDict[str(genre_id)] = 0
    
    def generateRefinedGenres(self):
        # for film in self.filmListe:
        #     film.refinedGenres = self.genreDict
        #     for genre in film.rawGenres:
        #         print(genre)
        #         film.refinedGenres[str(genre)] = 1
        for genre in self.genreDict.keys():
            for film in self.filmListe:
                if int(genre) in film.rawGenres:
                    film.refinedGenres[genre] = 1
                else:
                    film.refinedGenres[genre] = 0

                


class Film:
    def __init__(self, name, genres, rating, popularity):
        self.name = name #Filmens navn
        self.rawGenres = genres #liste over genrer denne film har.
        self.rawGenresDict = {}
        self.refinedGenres = {} #dict over alle genrer vi har set, samt om denne film har dem
        self.rating = rating
        self.pop = popularity
        



            

    
         
    @staticmethod
    def genreDistance(movie1Genres,movie2Genres):
        return
