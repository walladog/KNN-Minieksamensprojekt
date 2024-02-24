
alleGenrer = {}

class Film:
    def __init__(self, name, genres, rating, popularity):
        self.name = name #Filmens navn
        self.rawGenres = genres #Liste over genrer denne film har.
        self.refinedGenres = alleGenrer
        self.rating = rating
        self.pop = popularity
    
    def generateGenreList(self):
        for genre in self.rawGenres:
            if genre['name'] in alleGenrer:
                self.refinedGenres[genre['name']] = 1
                return
            else:
                alleGenrer[genre['name']] = 0
                self.refinedGenres[genre['name']] = 1



            


    @staticmethod
    def genreDistance(movie1Genres,movie2Genres):
        return
