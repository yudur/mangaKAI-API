import httpx
from fastapi import status

def test_expects_the_request_status_to_be_200():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/recommended")
    assert res.status_code == status.HTTP_200_OK