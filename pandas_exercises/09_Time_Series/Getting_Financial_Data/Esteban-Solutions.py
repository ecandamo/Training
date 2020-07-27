# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import datetime as dt
# Step 2. Create your time range (start and end variables). The start date should be 01/01/2015 and the end should today (whatever your today is)
start = dt.datetime(year=2015, month=1, day=1)
start = dt.datetime.today()
# Step 3. Select the Apple, Tesla, Twitter, IBM, LinkedIn stocks symbols and assign them to a variable called stocks
stocks = ['APPL', 'TSLA', 'TWTR', 'IBM']
# Step 4. Read the data from google, assign to df and print it
# Step 5.  What is the type of structure of df ?
# Step 6. Print all the Items axis values
# Step 7. Good, now we know  the data avaiable. Create a dataFrame called vol, with the Volume values.
# Step 8. Aggregate the data of Volume to weekly
# Hint: Be careful to not sum data from the same week of 2015 and other years.
# Step 9. Find all the volume traded in the year of 2015
