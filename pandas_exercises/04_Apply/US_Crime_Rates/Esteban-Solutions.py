# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv).
# Step 3. Assign it to a variable called crime.
# Step 4. What is the type of the columns?
# Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
# Step 5. Convert the type of the column Year to datetime64
# Step 6. Set the Year column as the index of the dataframe
# Step 7. Delete the Total column
# Step 8. Group the year by decades and sum the values
# Pay attention to the Population column number, summing this column is a mistake
# Step 9. What is the most dangerous decade to live in the US?
