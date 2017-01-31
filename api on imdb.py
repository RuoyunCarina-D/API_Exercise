
# read IMDb data into a DataFrame: we want a year column!
import pandas as pd

movies = pd.read_csv('imdb_1000.csv')
movies.head() 

# use requests library to interact with a URL
import requests
r = requests.get('http://www.omdbapi.com/?t=the shawshank redemption&r=json&type=movie')
r.status_code
r.text

# decode the JSON response body into a dictionary
r.json()

# extracting the year from the dictionary
r.json()['Year']

# what happens if the movie name is not recognized?
r = requests.get('http://www.omdbapi.com/?t=blahblahblah&r=json&type=movie')
r.status_code
r.json()

# define a function to return the year
def get_movie_year(title):
    r = requests.get('http://www.omdbapi.com/?t=' + title + '&r=json&type=movie')
    info = r.json()
    if info['Response'] == 'True':
        return int(info['Year'])
    else:
        return None

# test the function
get_movie_year('The Shawshank Redemption')
get_movie_year('blahblahblah')

# create a smaller DataFrame for testing
top_movies = movies.head().copy()

# write a for loop to build a list of years
from time import sleep
years = []
for title in top_movies.title:
    years.append(get_movie_year(title))
    sleep(1)

# check that the DataFrame and the list of years are the same length
assert(len(top_movies) == len(years))

# save that list as a new column
top_movies['year'] = years
