# Web-Scrapping
A simple web scrapping project that gets information from a website and store them in CSV files.

# Planning
- Going to scrap movies from https://www.themoviedb.org/
- Going to get the top 20 movies from three movies selections: 
  - Popular
  - Now playing
  - Upcoming
- For each movie, I will get
  - the user rating
  - trailer URL
  - top cast
  - movie name
  - certification
  - release date
  - genres
  - runtime
- For each selection, I will create a CSV file with the following format:
```
Movie Name,User Rating,Genres,Trailer URL,Top Cast,Runtime,Certification,Release Date
Spider-Man: No Way Home,84%,Action Adventure Science Fiction,https://www.themoviedb.org/movie/634649-spider-man-no-way-home#,Tom Holland Zendaya Benedict Cumberbatch Jacob Batalon Jon Favreau,2h 28m,PG-13,12/17/2021 (US)
```
