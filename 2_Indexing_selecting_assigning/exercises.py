import pandas as pd

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Look at an overview of your data by running the following line.
reviews.head()

# 1. Select the description column from reviews and assign the result to the variable desc.
desc = reviews.desription
desc = reviews["description"]

# 2. Select the first value from the description column of reviews, assigning it to variable first_description.
first_description = reviews["description"][0]
first_description = reviews.description.iloc[0]  # preferred way
first_description = reviews.description.loc[0]
first_description = reviews.description[0]

# 3. Select the first row of data (the first record) from reviews, assigning it to the variable first_row.
first_row = reviews.iloc[0]

# 4. Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.
# Hint: format your output as a pandas Series.
first_descriptions = reviews.description.iloc[:10]
first_descriptions = reviews.loc[:9, "description"]
first_descriptions = desc.head(10)

# 5. Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

# 6. Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100
cols = ["country", "province", "region_1", "region_2"]
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

# 7. Create a variable df containing the country and variety columns of the first 100 records.
cols = ["country", "variety"]
df = reviews.loc[:99, cols]
cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]

# 8. Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines = reviews.loc[reviews.country == "Italy"]

# 9. Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
top_oceania_wines = reviews.loc[
    (reviews.country.isin(["Australia", "New Zealand"])) & (reviews.points >= 95)
]
