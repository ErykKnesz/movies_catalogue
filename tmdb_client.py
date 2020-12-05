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


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}/{size}/{poster_api_path}"


def get_movies(list_type='popular', how_many=8):
    data = call_tmdb_api(f"movie/{list_type}")
    #data = random.sample(data['results'], len(data['results']))
    return data#[:how_many]

get_movies(list_type='popular', how_many=8)
def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id):
    data = call_tmdb_api(f"movie/{movie_id}/credits")
    return data['cast']


def search_movies(search_query):
    data = call_tmdb_api(f"search/movie/?query={search_query}")
    return data['results']


def get_series_airing_today():
    data = call_tmdb_api(f"tv/airing_today?")
    return data['results']