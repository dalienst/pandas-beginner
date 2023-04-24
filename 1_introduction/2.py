# Reading data
import pandas as pd

wine_reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv")

# See how large the dataframe is
print(wine_reviews.shape)

# Examine the data
print(wine_reviews.head())

# Make pandas use the default index by specifying index_col
wine_reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.head())
