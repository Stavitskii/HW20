from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="John")
    d2 = Director(id=2, name="Johan")
    d3 = Director(id=3, name="Jon")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(return_value=d3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(id=1, name="Comedy")
    genre2 = Genre(id=2, name="Thriller")
    genre3 = Genre(id=3, name="Drama")

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2])
    genre_dao.create = MagicMock(return_value=genre3)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao





