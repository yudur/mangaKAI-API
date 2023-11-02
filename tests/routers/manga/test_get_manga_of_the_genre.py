import httpx
from fastapi import status

def test_expect_a_status_of_200_and_a_pagination_greater_than_50():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/genres/acao/3")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert data["pagination"] > 50

def test_accessing_a_genre_that_doesn_t_exist():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/genres/test_teste/1")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert data == {"results": [], "pagination": 0}

def test_accessing_a_page_larger_than_the_one_available():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/genres/acao/999")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert data == {"results": [], "pagination": 0}