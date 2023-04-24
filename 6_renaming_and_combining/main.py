import pandas as pd

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# RENAMING
print(reviews.rename(columns={"points": "score"}))
print(reviews.rename(index={0: "firstEntry", 1: "secondEntry"}))
print(reviews.rename_axis("wines", axis="rows").rename_axis("fields", axis="columns"))


# COMBINING
# concat()
# join()
# merge()
