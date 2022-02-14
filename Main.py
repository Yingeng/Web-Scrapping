import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

needed_headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
website_url = ["https://www.themoviedb.org/movie", "https://www.themoviedb.org/movie/now-playing", "https://www.themoviedb.org/movie/upcoming"]
base_url = "https://www.themoviedb.org"
base_youtube_url = "https://www.youtube.com/watch?v="

movie_urls = [[], [], []]
movie_names = [[], [], []]
movie_user_ratings = [[], [], []]
movie_top_casts = [[], [], []]
movie_certifications = [[], [], []]
movie_runtimes = [[], [], []]
movie_trailer_urls = [[], [], []]
movie_genres = [[], [], []]
movie_release_dates = [[], [], []]
movie_overviews = [[], [], []]


def get_movie_info(url, selection):
    movie_txt = requests.get(base_url+url, headers=needed_headers).text
    soup_movie = BeautifulSoup(movie_txt, "lxml")
    try:
        certification = soup_movie.find("span", class_="certification").text.strip()
    except:
        certification = "N/A"
    release_date = soup_movie.find("span", class_="release").text.strip()
    genres = []
    genres_span = soup_movie.find("span", class_="genres").find_all("a")
    for genre_span in genres_span:
        genres.append(genre_span.text.strip())
    overview = soup_movie.find("div", class_="overview").text.strip()
    try:
        runtime = soup_movie.find("span", class_="runtime").text.strip()
    except:
        runtime = "N/A"
    try:
        trailer_url = base_youtube_url + soup_movie.find("a", {"data-site": "YouTube"})["data-id"]
    except:
        trailer_url = "N/A"
    rating = re.findall(r"\d+", soup_movie.find("div", class_="percent").contents[1]["class"][1])
    if len(rating) == 0:
        rating = 0
    else:
        rating = "NR"
    casts = []
    cast_cards = soup_movie.find_all("li", class_="card")
    for cast_card in cast_cards:
        casts.append(cast_card.contents[3].text.strip())
    movie_certifications[selection].append(certification)
    movie_release_dates[selection].append(release_date)
    movie_trailer_urls[selection].append(trailer_url)
    movie_genres[selection].append(genres)
    movie_runtimes[selection].append(runtime)
    movie_user_ratings[selection].append(rating)
    movie_top_casts[selection].append(casts)
    movie_overviews[selection].append(overview)


def movie_selection(url, selection):
    html_txt = requests.get(url, headers=needed_headers).text
    soup = BeautifulSoup(html_txt, "lxml")
    movies = soup.find_all("a", class_="image")
    for movie in movies:
        movie_urls[selection].append(base_url + movie["href"])
        movie_names[selection].append(f'{movie["title"]}')
        get_movie_info(movie["href"], selection)

    movies_dict = {
        "Movie Name": movie_names[selection],
        "User Rating": movie_user_ratings[selection],
        "Genres": movie_genres[selection],
        "Trailer URL": movie_trailer_urls[selection],
        "Top Casts": movie_top_casts[selection],
        "Runtime": movie_runtimes[selection],
        "Certification": movie_certifications[selection],
        "Release Date": movie_release_dates[selection],
        "Overview": movie_overviews[selection],
        "Movie URL": movie_urls[selection],
    }

    movies_df = pd.DataFrame(movies_dict)
    if selection == 0:
        movies_df.to_csv("popular_movies.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", doublequote=False,
                         index=False)
        print("Popular Movies Finished Processing!")
    elif selection == 1:
        movies_df.to_csv("now_playing_movies.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", doublequote=False,
                         index=False)
        print("Current Playing Movies Finished Processing!")
    else:
        movies_df.to_csv("upcoming_movies.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", doublequote=False,
                         index=False)
        print("Upcoming Movies Finished Processing!")


if __name__ == "__main__":
    for i in range(3):
        movie_selection(website_url[i], i)
