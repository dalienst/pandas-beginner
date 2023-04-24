import pandas as pd

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# 1. What is the data type of the points column in the dataset?
dtype = reviews.points.dtype

# 2. Create a Series from entries in the points column, but convert the entries to strings. 
# Hint: strings are str in native Python.
point_strings = reviews.points.astype("str")

# 3. Sometimes the price column is null. 
# How many reviews in the dataset are missing a price?
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()

# 4. What are the most common wine-producing regions? 
# Create a Series counting the number of times each value 
# occurs in the region_1 field. This field is often missing data, 
# so replace missing values with Unknown. Sort in descending order. 
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)