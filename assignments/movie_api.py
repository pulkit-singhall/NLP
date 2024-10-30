import os
import requests # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

tmdb_access_token = os.getenv('TMDB_ACCESS_TOKEN')
tmdb_api_key = os.getenv('TMDB_API_KEY')


# getting json response from TMDB API
def getJsonDescription():
    tot_pages = 20
    headers = {
        "accept": "application/json",
        "Authorization": f'Bearer {tmdb_access_token}'
    }

    descriptionList = []

    for i in range(tot_pages):
        page = i+1
        url = f'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}'
        response = requests.get(url=url, headers=headers)
        json = response.json()
        results = json['results']

        for movie in results:
            desc = movie['overview']
            descriptionList.append(desc)

    return descriptionList