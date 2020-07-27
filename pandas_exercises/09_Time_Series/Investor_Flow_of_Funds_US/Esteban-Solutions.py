# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import datetime as dt
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv).
file = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
# Step 3. Assign it to a variable calledm funds
funds = pd.read_csv(file)
funds.head()
# Step 4.  What is the frequency of the dataset?
funds.shape
# Step 5. Set the column Date as the index.
funds = funds.set_index('Date')
# Step 6. What is the type of the index?
funds.index.dtype
# Step 7. Set the index to a DatetimeIndex type
funds.index = funds.index.astype('datetime64[ns]')
# Step 8.  Change the frequency to monthly, sum the values and assign it to monthly.
funds.index.dtype
# Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.
funds = funds.dropna(axis=0)
# Step 10. Good, now we have the monthly data. Now change the frequency to year.
