import pandas as pd

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Native accessor
print(reviews.country)
print(reviews["country"])
print(reviews["country"][0])

# Indexing in pandas - iloc and loc

# 1. Index-based selection - iloc
print(reviews.iloc[0])  # selecting the first row of data
print("")
# getting a column
print(reviews.iloc[:, 0])
print("")
print(reviews.iloc[[0, 1, 2], 0])
print("")
# This will start counting forwards from the end of the values.
print(reviews.iloc[-5:])
print("")

# 2. Label-based selection - loc
print(reviews.loc[0, "country"])
print("")
print(reviews.loc[:, ["taster_name", "taster_twitter_handle", "points"]])
print("")


# MANIPULATING THE INDEX
print(reviews.set_index("title"))
print("")


# CONDITIONAL SELECTION
print(reviews.country == "Italy")
print("")
print(reviews.loc[reviews.country == "Italy"])
print("")
print(reviews.loc[(reviews.country == "Italy") & (reviews.points >= 90)])
print()
print(reviews.loc[(reviews.country == "Italy") | (reviews.points >= 90)])

# isin
print(reviews.loc[reviews.country.isin(["Italy", "France"])])

# isnull notnull
print(reviews.loc[reviews.price.notnull()])


# ASSIGNING DATA
reviews["critic"] = "everyone"
print(reviews["critic"])

reviews["index_backwards"] = range(len(reviews), 0, -1)
print(reviews["index_backwards"])
