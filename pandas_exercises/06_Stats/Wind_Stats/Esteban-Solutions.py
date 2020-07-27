# The data in 'wind.data' has the following format:
"""
Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
61  1  1 15.04 14.96 13.17  9.29   NaN  9.87 13.67 10.25 10.83 12.58 18.50 15.04
61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71
"""
#    The first three columns are year, month and day.  The
#    remaining 12 columns are average windspeeds in knots at 12
#    locations in Ireland on that day.
# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import datetime as dt
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data)
file = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
# Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.
data = pd.read_table(file, sep='\s+', parse_dates = [['Yr','Mo','Dy']])
# Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.
change_year = lambda x: dt.date(x.year-100,x.month,x.day) if x.year>1978 else dt.date(x.year,x.month,x.day)
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(change_year).astype('datetime64')
# Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].
data = data.set_index('Yr_Mo_Dy')
# Step 6. Compute how many values are missing for each location over the entire record.
data.isnull().sum()
# Step 7. Compute how many non-missing values there are in total.
data.notnull().sum()
# Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
data.agg('mean').agg('mean')
# Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
loc_stats = data.agg(['min','max','mean'])
# Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
day_stats = data.agg(['min','max','mean'], axis = 1)
# Step 11. Find the average windspeed in January for each location.
data[data.index.month == 1].agg(['mean'])
# Step 12. Downsample the record to a yearly frequency for each location.
data.groupby(data.index.year).sum()
# Step 13. Downsample the record to a monthly frequency for each location.
data.groupby(data.index.month).sum()
# Step 14. Downsample the record to a weekly frequency for each location.
data.groupby(data.index.week).sum()
# Step 15. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.
