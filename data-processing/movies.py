import requests


class Movie:
    def __init__(self, title, year, poster_url):
        self.title = title
        self.year = year
        self.poster_url = poster_url


class OMDBMoviesClient:
    def __init__(self, url, token):
        self.base_url = url + "?apikey=" + token + "&t="

    def get_movie_details(self, title, year):
        address = self.base_url + "&t=" + title + "&year=" + str(year)
        r = requests.get(address, auth=("user", "pass"))
        json = r.json()
        return Movie(json["Title"], year, json["Poster"])

