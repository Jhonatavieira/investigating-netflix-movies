import pandas as pd
import matplotlib.pyplot as plt


netflix_df = pd.read_csv("netflix_data.csv")

print(netflix_df.columns)

# Filtering just movies
netflix_subset = netflix_df[netflix_df['type'] == "Movie"]

# Filtering release before 1990s and less 2000
movies_1990s = netflix_df[(netflix_df["release_year"] >= 1990) & (
    netflix_df["release_year"] < 2000)]

movies_1990s.to_csv("movies_1990s.csv")

plt.hist(movies_1990s["duration"])
plt.title("Distribuition of Movie duration in the 1990s")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.show()

action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

short_movie_count = 0

for lab, row in action_movies_1990s.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count


action_movies_1990s.to_csv("action_movies_1990s.csv")

print(short_movie_count)
