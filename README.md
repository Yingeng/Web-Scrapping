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
  - movie URL
  - Overview
- For each selection, I will create a CSV file with the following format:
```
"Movie Name","User Rating","Genres","Trailer URL","Top Casts","Runtime","Certification","Release Date","Overview","Movie URL"
"Spider-Man: No Way Home","NR","['Action', 'Adventure', 'Science Fiction']","https://www.youtube.com/watch?v=JfVOs4VSpmA","['Tom Holland', 'Zendaya', 'Benedict Cumberbatch', 'Jacob Batalon', 'Jon Favreau', 'Jamie Foxx', 'Willem Dafoe', 'Alfred Molina', 'Benedict Wong']","2h 28m","PG-13","12/17/2021 (US)","Peter Parker is unmasked and no longer able to separate his normal life from the high-stakes of being a super-hero. When he asks for help from Doctor Strange the stakes become even more dangerous, forcing him to discover what it truly means to be Spider-Man.","https://www.themoviedb.org/movie/634649"
```
