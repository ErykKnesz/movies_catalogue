import requests
import random

api_token = ("eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIy"
    "NzhmYTU0NjI2ZDY0YzliMDc2MTI2ZGM1NzJhNGYwZiIsIn"
    "N1YiI6IjVmYTFhODQ0Njc4MjU5MDAzNTlmMzQ1MyIsInNj"
    "b3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xbO"
    "z0JOFdwjDpNRTl_Dt97wqluj7Lzy5LMOdivi3ETI")
headers = {
    'Authorization': f"Bearer {api_token}"
}


def get_poster_url(poster_api_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return base_url + f"/{size}/" + poster_api_path


def get_movies(list_type='popular', how_many=12):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    data = response.json()
    data = random.sample(data['results'], len(data['results']))
    return data[:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast']