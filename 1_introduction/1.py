# Creating data
import pandas as pd

# 1. The DataFrame - a table containing an array of elements
num = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
print(num)

character = pd.DataFrame(
    {"Bob": ["I liked it.", "It was awful."], "Sue": ["Pretty good.", "Bland."]}
)
print(character)

labels = pd.DataFrame(
    {"Bob": ["I liked it.", "It was awful."], "Sue": ["Pretty good.", "Bland."]},
    index=["Product A", "Product B"],
)
print(labels)

#  2. Series - a sequence of data values/ a list
series1 = pd.Series([1, 2, 3, 4, 5])
print(series1)

ser_labels = pd.Series(
    [30, 35, 40], index=["2015 Sales", "2016 Sales", "2017 Sales"], name="Product A"
)
print(ser_labels)