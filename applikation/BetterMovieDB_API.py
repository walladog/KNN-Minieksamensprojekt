import requests
import json

# Define the API key and the Bearer token
api_key = '6946f0d386c93f0382df916068e76b28'
bearer_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2OTQ2ZjBkMzg2YzkzZjAzODJkZjkxNjA2OGU3NmIyOCIsInN1YiI6IjY1ZDg1ZWMyMTQ5NTY1MDE3YmY1ZWVmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Q1ebIcJom7_6odxlkg5yNqXH3vacAQUUukPz9N3Zkk'

# Define the URL for the request
base_url = 'https://api.themoviedb.org/3/search/movie'

def findFilm(filmName):
    #FilmName = 'forest gump'

    # Define the parameters for the request
    params = {
        'api_key': api_key,
        # Replace with the name of the movie you're searching for
        f'query': {filmName}
    }
    # Define the headers for the request
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }

    # Make the GET request
    return  requests.get(base_url, params=params, headers=headers).json()['results'][0]

# Print the response
#print(json.dumps(response.json(), ensure_ascii=False).encode('utf8'))
#Note fra ASKE: Jeg aner ikke hvad fuck det her er, men det er irriterende, så jeg har slettet. Fuck dig Artem :)

#print(response.json()['results'][0]['original_title'])
#print(response)
