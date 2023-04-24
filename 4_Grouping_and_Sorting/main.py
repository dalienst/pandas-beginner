import pandas as pd

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews.groupby("points").points.count())

# cheapest wine in each point value category
print(reviews.groupby("points").price.min())

# one way of selecting the name of the first wine reviewed from
# each winery in the dataset:
print(reviews.groupby("winery").apply(lambda df: df.title.iloc[0]))

# here's how we would pick out the best wine by country and province:
print(
    reviews.groupby(["country", "province"]).apply(
        lambda df: df.loc[df.points.idxmax()]
    )
)

# agg() - which lets you run a bunch of different functions on your DataFrame simultaneously.
# we can generate a simple statistical summary of the dataset as follows:
print(reviews.groupby(["country"]).price.agg([len, min, max]))


# MULTI-INDEXES
countries_reviewed = reviews.groupby(["country", "province"]).description.agg([len])
print(countries_reviewed)
mi = countries_reviewed.index
print(type(mi))

print(countries_reviewed.reset_index())


# SORTING
countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed.sort_values(by="len"))
print(countries_reviewed.sort_values(by="len", ascending=False))
# sorting by index values
print(countries_reviewed.sort_index())
# sorting by more than one column at a time
print(countries_reviewed.sort_values(by=["country", "len"]))
