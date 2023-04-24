import pandas as pd

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)


# DATA TYPES
print(reviews.price.dtype)
print(reviews.dtypes)
print(reviews.points.astype("float64"))
# dtype for series or dataframe
print(reviews.index.dtype)


# MISSING DATA
# selecting NaN entries
print(reviews[pd.isnull(reviews.country)])
# Replacing missing values
print(reviews.region_2.fillna("Unknown"))
print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))
