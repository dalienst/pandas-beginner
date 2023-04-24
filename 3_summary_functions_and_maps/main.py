import pandas as pd
import numpy as np

pd.set_option("display.max_rows", 5)

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)

# SUMMARY FUNCTIONS
print(reviews.points.describe())
print(reviews.taster_name.describe())
print(reviews.points.mean())
print(reviews.taster_name.unique())
print(reviews.taster_name.value_counts())


# MAPS
# 1. map()
# suppose that we wanted to remean the scores the wines received to 0suppose that we wanted to remean the scores the wines received to 0
review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p: p - review_points_mean))

# apply() is the equivalent method if we want to transform a whole
# DataFrame by calling a custom method on each row.
def remean_points(row):
    row.points = row.points - review_points_mean
    return row


print(reviews.apply(remean_points, axis="columns"))

# Pandas provides many common mapping operations as built-ins. For example,
# here's a faster way of remeaning our points column:
review_points_mean = reviews.points.mean()
print(reviews.points - review_points_mean)
