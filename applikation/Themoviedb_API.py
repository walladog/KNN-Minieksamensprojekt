import requests

# Define the API key and the Bearer token
api_key = '6946f0d386c93f0382df916068e76b28'
bearer_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2OTQ2ZjBkMzg2YzkzZjAzODJkZjkxNjA2OGU3NmIyOCIsInN1YiI6IjY1ZDg1ZWMyMTQ5NTY1MDE3YmY1ZWVmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Q1ebIcJom7_6odxlkg5yNqXH3vacAQUUukPz9N3Zkk'

film_id = 13


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
response = requests.get(base_url, params=params, headers=headers)

# Print the response
print(response.json())
