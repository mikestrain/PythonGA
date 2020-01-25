import pandas
import matplotlib
import numpy
import sklearn

import pandas as pd

file_name = 'mpg.csv'
df = pd.read_csv(file_name) # creates data frame or "df"

# a DATAFRAME is made of multiple SERIES

print(df.head(2)) # method that prints by default the first 5 rows
print(df.tail(2)) # method that prints by default the last 5 rows
print(df.shape) # the shape of the table is a Tuple! (R, C)
print(list(df.columns))

print(df["horsepower"]) # this is something called a "series", not a list!
print(list(df["cylinders"])) # this is a list

print(df["cylinders"].mean())

print(df.dtypes) # this is how you can see what Pandas thinks of an object.

print(df.describe()) # VERY nice way of seeing a summary of the CSV table.

print(df.info()) # some info about the table.