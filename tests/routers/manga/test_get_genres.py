import httpx
from fastapi import status

def test_getting_the_data_correctly_with_a_status_of_200():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/genres")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()

    assert "Ação" in data["genres"]