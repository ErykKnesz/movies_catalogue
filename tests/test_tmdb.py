import sys
sys.path.append("C:\\Users\\Dagmara\\Desktop\\kodilla\\Python\\Projekty\\"
                 "movies_project\\movies_catalogue")

import tmdb_client
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
    poster_api_path = "https://image.tmdb.org/t/p/w342/some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url

    
def test_get_movies_not_none():
    movies_lists = ['popular', 'now_playing', 'top_rated', 'upcoming']
    responses = []
    for list_type in movies_lists:
        response = tmdb_client.get_movies(list_type=list_type)
        responses.append(response)
    assert None not in responses
    

def test_get_single_movie_not_none():
    response = tmdb_client.get_single_movie(650747)
    assert response is not None


def test_get_single_movie_cast_not_none():
    response = tmdb_client.get_single_movie_cast(650747)
    assert response is not None


def test_get_search_movies_not_none():
    response = tmdb_client.search_movies('Hard kill')
    assert response is not None


def test_get_series_airing_today():
    response = tmdb_client.get_series_airing_today()
    assert response is not None    


def test_call_tmdb_api_for_content(monkeypatch):
    mock_api = 'mock'
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_api
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    api = tmdb_client.call_tmdb_api(tmdb_client.get_movies())
    assert api == mock_api