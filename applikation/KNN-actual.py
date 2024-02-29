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

import requests

# Define the API key and the Bearer token
api_key = '6946f0d386c93f0382df916068e76b28'
bearer_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2OTQ2ZjBkMzg2YzkzZjAzODJkZjkxNjA2OGU3NmIyOCIsInN1YiI6IjY1ZDg1ZWMyMTQ5NTY1MDE3YmY1ZWVmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Q1ebIcJom7_6odxlkg5yNqXH3vacAQUUukPz9N3Zkk'

film_id = 13
fimd_id = 15


# Define the URL for the request
base_url = f'https://api.themoviedb.org/3/movie/{film_id}'

# Define the parameters for the request
params = {
    'api_key': api_key,
    'append_to_response': 'videos,images'
}

# Define the headers for the request
headers = {
    'Authorization': f'Bearer {bearer_token}'
}

# Make the GET request
response = requests.get(base_url, params=params, headers=headers).json()
print(response['original_title'])

film = Film(response['original_title'],response['genres'],response['vote_average'],response['vote_count'])

print(film.rawGenres)

print(genreDict)
film.generateRefinedGenres()
print(film.refinedGenres)