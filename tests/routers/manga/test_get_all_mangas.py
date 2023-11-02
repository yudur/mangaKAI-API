import httpx
from fastapi import status

def test_get_all_the_manga_successfully():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/page/1")
    assert res.status_code == status.HTTP_200_OK

def test_expect_a_404_error_as_paging_exceeded_limits():
    with httpx.Client() as client:
        res = client.get("http://127.0.0.1:8000/api/manga/page/99999")
    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json() == {"detail": "Page not found"}