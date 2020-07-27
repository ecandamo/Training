# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import datetime as dt
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)
file = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
# Step 3. Assign it to a variable apple
apple = pd.read_csv(file)
# Step 4.  Check out the type of the columns
apple.dtypes
# Step 5. Transform the Date column as a datetime type
apple['Date'] = pd.to_datetime(apple['Date'])
apple.dtypes
# Step 6.  Set the date as the index
apple = apple.set_index('Date')
apple.index
# Step 7.  Is there any duplicate dates?
apple.index.value_counts().sum()
apple.index.nunique()
# Step 8.  Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
apple = apple.sort_index(ascending=True)
# Step 9. Get the last business day of each month

# Step 10.  What is the difference in days between the first day and the oldest
apple.index.max()-apple.index.min()
# Step 11.  How many months in the data we have?
apple.index.datetime()
# Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
