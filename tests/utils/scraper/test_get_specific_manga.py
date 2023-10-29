import pytest
from src.utils.scraper import get_specific_manga

mangas_errors = [
    "123456789"
    "testeTeste-Teste"
]

def test_I_hope_the_ValueError_exception_returns_because_I_passed_an_invalid_route():
    for manga in mangas_errors:
        with pytest.raises(ValueError):
            get_specific_manga(manga)