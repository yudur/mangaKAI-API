from fastapi import status
import httpx
import ast

def test_the_data_is_being_returned_correctly_through_the_HTTP_streaming_call():
    expected_pages = [
        'https://viralcontentmxp.xyz/uploads/o/otagai-sukoshi-zutsu-kawatteiku-kyouikugakari-to-shinnyuushain/1/1',
        'https://viralcontentmxp.xyz/uploads/o/otagai-sukoshi-zutsu-kawatteiku-kyouikugakari-to-shinnyuushain/1/2',
        'https://viralcontentmxp.xyz/uploads/o/otagai-sukoshi-zutsu-kawatteiku-kyouikugakari-to-shinnyuushain/1/3',
        'https://viralcontentmxp.xyz/uploads/o/otagai-sukoshi-zutsu-kawatteiku-kyouikugakari-to-shinnyuushain/1/4'
    ]
    manga_pages = []

    with httpx.Client() as client:
        with client.stream('GET', "http://127.0.0.1:8000/api/manga/read/otagai-sukoshi-zutsu-kawatteiku-kyouikugakari-to-shinnyuushain-1-online") as res:
            assert res.status_code == status.HTTP_200_OK

            for line in res.iter_text():
                if line == "finished application":
                    break

                manga_pages.append(line)
        
        assert manga_pages == expected_pages
                
def test_expect_a_404_error_because_the_url_is_invalid():
    with httpx.Client() as client:
        with client.stream('GET', "http://127.0.0.1:8000/api/manga/read/teste-404error") as  res:
            assert res.status_code == status.HTTP_404_NOT_FOUND

            for line in res.iter_lines():
                assert ast.literal_eval(line) == {"detail":"non-existent chapter"}
                break
