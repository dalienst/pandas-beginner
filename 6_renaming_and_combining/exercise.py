import pandas as pd

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

reviews.head()

# 1. region_1 and region_2 are pretty uninformative names for locale
# columns in the dataset. Create a copy of reviews with these columns
# renamed to region and locale, respectively.
renamed = reviews.rename(columns={"region_1": "region", "region_2": "locale"})

# 2. Set the index name in the dataset to wines
reindexed = reviews.rename_axis("wines", axis="rows")
