import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

needed_headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
website_url = ["https://www.themoviedb.org/movie", "https://www.themoviedb.org/movie/now-playing",
               "https://www.themoviedb.org/movie/upcoming"]
filenames = ["popular_movies", "now_playing_movies", "upcoming_movies"]
base_url = "https://www.themoviedb.org"
base_youtube_url = "https://www.youtube.com/watch?v="


def get_movie_info(url):
    movie_txt = requests.get(base_url + url, headers=needed_headers).text
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
    return certification, release_date, trailer_url, genres, runtime, rating, casts, overview


def movie_selection(url, filename):
    movie_urls = []
    movie_names = []
    movie_user_ratings = []
    movie_top_casts = []
    movie_certifications = []
    movie_runtimes = []
    movie_trailer_urls = []
    movie_genres = []
    movie_release_dates = []
    movie_overviews = []
    html_txt = requests.get(url, headers=needed_headers).text
    soup = BeautifulSoup(html_txt, "lxml")
    movies = soup.find_all("a", class_="image")
    for movie in movies:
        movie_urls.append(base_url + movie["href"])
        movie_names.append(f'{movie["title"]}')
        movie_info = get_movie_info(movie["href"])
        populate_list(movie_user_ratings, movie_top_casts, movie_certifications, movie_runtimes,
                      movie_trailer_urls, movie_genres, movie_release_dates, movie_overviews, movie_info)

    movies_dict = {
        "Movie Name": movie_names,
        "User Rating": movie_user_ratings,
        "Genres": movie_genres,
        "Trailer URL": movie_trailer_urls,
        "Top Casts": movie_top_casts,
        "Runtime": movie_runtimes,
        "Certification": movie_certifications,
        "Release Date": movie_release_dates,
        "Overview": movie_overviews,
        "Movie URL": movie_urls,
    }

    movies_df = pd.DataFrame(movies_dict)
    movies_df.to_csv(f"./CSVs/{filename}.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", doublequote=False,
                     index=False)
    print(f"{filename}.csv Generated!")


def populate_list(movie_user_ratings, movie_top_casts, movie_certifications, movie_runtimes,
                  movie_trailer_urls, movie_genres, movie_release_dates, movie_overviews, movie_info):
    movie_certifications.append(movie_info[0])
    movie_release_dates.append(movie_info[1])
    movie_trailer_urls.append(movie_info[2])
    movie_genres.append(movie_info[3])
    movie_runtimes.append(movie_info[4])
    movie_user_ratings.append(movie_info[5])
    movie_top_casts.append(movie_info[6])
    movie_overviews.append(movie_info[7])


if __name__ == "__main__":
    for i in range(3):
        movie_selection(website_url[i], filenames[i])
