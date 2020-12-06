import sys
sys.path.append("C:\\Users\\Dagmara\\Desktop\\kodilla\\Python\\Projekty\\"
                 "movies_project\\movies_catalogue")

import tmdb_client
from main import app
from unittest.mock import Mock, MagicMock
import pytest

@pytest.mark.parametrize('selected_list', (
    ('popular'),
    ('now_playing'),
    ('top_rated'),
    ('upcoming')
))
def test_homepage(monkeypatch, selected_list):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response_with_query = client.get(f'/?list_type={selected_list}')
        assert response_with_query.status_code == 200
        api_mock.assert_called_with(f'movie/{selected_list}')


def test_call_tmdb_api(monkeypatch):
    mock_api = {
        'results': [{'k1': 'v1'}]
    }
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_api
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    api = tmdb_client.get_movies('popular')
    assert api == mock_api['results']


def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url


def test_get_movies_is_8(monkeypatch):
    mock_result = [
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'}
    ]
    api_mock = MagicMock(return_value=mock_result)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    assert len(api_mock()) == 8


def test_get_movies_is_random(monkeypatch):
    mock_result = [
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'},
        {'k1': 'v1'}
    ]
    api_mock_1 = MagicMock(return_value=mock_result)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock_1)
    api_mock_2 = MagicMock(return_value=mock_result)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock_2)
    assert api_mock_1 != api_mock_2


def test_get_single_movie_cast(monkeypatch):
    mock_data = {'cast': 'some cast'}
    api_mock = Mock(return_value=mock_data)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    assert 'cast' in api_mock().keys()


def test_get_search_movies(monkeypatch):
    mock_data = {'results': 'some results'}
    api_mock = Mock(return_value=mock_data)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    assert 'results' in api_mock().keys()


def test_get_series_airing_today(monkeypatch):
    mock_data = {'results': 'some results'}
    api_mock = Mock(return_value=mock_data)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    assert 'results' in api_mock().keys()