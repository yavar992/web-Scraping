import requests as re
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.imdb.com/chart/top/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


data = re.get(url=URL, headers=headers)

soup = BeautifulSoup(data.text , 'html.parser')

newData = soup.find('ul',class_='ipc-metadata-list--dividers-between')
# print(newData.text)

MovieName = []
Duration=[]
ReleaseYear = []
Rating =[]
NoOfRating = []

moviesName = newData.find_all('h3',class_='ipc-title__text')
# print(moviesName)

for i in moviesName:
    movie = i.text
    MovieName.append(movie)
# print(MovieName)   

metaDataItem = newData.find_all('span', class_='sc-b189961a-8 hCbzGp cli-title-metadata-item')

# Iterate through the list in steps of 3 to separate the values correctly
for i in range(0, len(metaDataItem), 3):
    # Extract release year if it is numeric (or check for valid year format)
    release_year = metaDataItem[i].text.strip()
    if release_year.isdigit() and len(release_year) == 4:  # Assuming valid year format
        ReleaseYear.append(release_year)
    
    # Extract duration if it contains 'h' (assuming all durations contain 'h')
    if i + 1 < len(metaDataItem):
        duration = metaDataItem[i + 1].text.strip()
        if 'h' in duration:  # Assuming valid duration format
            Duration.append(duration)


ratings = newData.find_all('span',class_='ipc-rating-star--rating')

for i in ratings:
    rating = i.text.strip()
    Rating.append(rating)


totalNoOfRatings = newData.find_all('span', class_='ipc-rating-star--voteCount')
for i in totalNoOfRatings:
    rate = i.text.strip()
    NoOfRating.append(rate)

# print(NoOfRating)    


df = pd.DataFrame({
    'Movie Name' : MovieName ,
    'Duration' : Duration ,
    'Release Year' : ReleaseYear,
    'Rating' : Rating ,
    'Total Rating' : NoOfRating
})

print(df.to_string(index= False))

