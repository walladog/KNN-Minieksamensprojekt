import BetterMovieDB_API

genreDict = {}


class Film:
    def __init__(self, name, genres, rating, popularity):
        self.name = name #Filmens navn
        self.rawGenres = genres #dict over genrer denne film har.
        self.addGenresToGenreDict() #Tjekker om filmen har nogen genrer som vi ikke har set endnu og tilføjer dem.
        self.refinedGenres = {} #dict over alle genrer vi har set, samt om denne film har dem
        self.rating = rating
        self.pop = popularity
        
    def addGenresToGenreDict(self):
        for genre in self.rawGenres:
            if genre['name'] in genreDict:
                pass
            else:
                genreDict[genre['name']] = 0

    def generateRefinedGenres(self):
        self.refinedGenres = genreDict
        for genre in self.rawGenres:
            self.refinedGenres[genre['name']] = 1
            pass
            

    
         
    @staticmethod
    def genreDistance(movie1Genres,movie2Genres):
        return

film = Film(response.json['name'])