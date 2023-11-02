# MangaKAI
Brazilian Restful API built with FastAPI ❤️

# Usage
1. Clone this repository
    ```bash
        git clone https://github.com/yudur/mangaKAI-API.git
    ```
2. Install dependecies (`pip install -r requirements.txt` or `pipenv install`)
3. Start the development environment
    ```bash
    uvicorn src.app:app or pipenv run start
    ```
4. visit http://localhost:8000/api/docs

# Documentation
__API__ __PATH__ = http://localhost:8000/api/docs
</br>__ApI__ Version = `v0.0.1`

## All Manga
Get Latest Manga Update
```
GET /manga/page/[pagenumber]
```
example : http://localhost:8000/api/manga/page/1

## Detail Manga
```
GET /manga/detail/[endpoint]
```
example : http://localhost:8000/api/manga/detail/hunter-x-hunter-online

# Read Manga
```
STREAM: GET /manga/read/[endpoint]
```
example : http://localhost:8000/api/manga/detail/otagai-sukoshi-zutsu-kawatteiku-kyouikugakari-to-shinnyuushain-1-online

## Search Manga by Name
```
GET manga/search/[query]
```
example : http://localhost:8000/api/manga/search/ota?pagenumber=2

## Genre List
```
GET /manga/genres
```
example : http://localhost:8000/api/genres

## Genre Detail
```
GET manga/genres/[endpoint]/[pagenumber]
```
example : http://localhost:8000/api/manga/genres/acao/1

## Recommended Manga
```
GET /manga/recommended
```
example : http://localhost:8000/api/manga/recommended