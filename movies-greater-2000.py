import pandas as np
import matplotlib.pyplot as plt

all_movies_df = np.read_csv("netflix_data.csv")

# filtering tv show
tv_show_movies = all_movies_df[all_movies_df["type"] == "TV Show"]

# Movies after 2000
movies_after_2000 = tv_show_movies[(tv_show_movies["release_year"] >= 2000)]

movies_after_2000[movies_after_2000[""]]

plt.clf()
plt.hist(movies_after_2000["duration"], 5)
plt.title("Distribuition of movies in the great than 2000")
plt.xlabel("Duration movies")
plt.ylabel("Number of movies")

movies_after_2000.to_csv("movies_after_2000.csv")

plt.show()
