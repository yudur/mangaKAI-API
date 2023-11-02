import httpx
from fastapi import status

def test_hope_that_all_data_is_returned_correctly():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/search/ota?pagenumber=20")
    data = res.json()

    assert res.status_code == status.HTTP_200_OK
    assert data["pagination"] > 50

def test_search_for_a_non_existent_manga_name():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/search/testetesteabcabc")
    data = res.json()

    assert data["results"] == []
    assert data["pagination"] == 0

def test_accessing_much_larger_pagination_than_available():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/search/ota?pagenumber=9999")
    data = res.json()

    assert data["results"] == []
    assert data["pagination"] == 0

def test_invalid_data_was_sent_in_the_pagenumber_field():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/search/ota?pagenumber=invalid")
    assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY