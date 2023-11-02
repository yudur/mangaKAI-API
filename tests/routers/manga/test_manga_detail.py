import httpx
from fastapi import status

def test_expects_all_data_to_be_returned_correctly():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/detail/hunter-x-hunter-online")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert data["title"] == "Ler Hunter x Hunter Online"

def test_expect_a_404_error_because_the_url_is_invalid():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/detail/nonexistent-manga-teste")
    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json() == {"detail": "non-existent manga"}