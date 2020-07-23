# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv).
file = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
# Step 3. Assign it to a variable called euro12.
euro = pd.read_csv(file)
euro.head()
# Step 4. Select only the Goal column.
euro.loc[:,['Goals']].head()
# Step 5. How many team participated in the Euro2012?
euro['Team'].nunique()
# Step 6. What is the number of columns in the dataset?
euro.columns.value_counts().sum()
# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro.loc[:,['Team','Yellow Cards','Red Cards']]
# Step 8. Sort the teams by Red Cards, then to Yellow Cards
discipline.sort_values(by='Red Cards').sort_values(by='Yellow Cards')
# Step 9. Calculate the mean Yellow Cards given per Team
euro.loc[:,'Yellow Cards'].agg('mean')
# Step 10. Filter teams that scored more than 6 goals
euro[euro['Goals']>6]
# Step 11. Select the teams that start with G
euro[euro['Team'].str.startswith('G')]
# Step 12. Select the first 7 columns
euro.iloc[:,:7]
# Step 13. Select all columns except the last 3.
euro.iloc[:,:-3]
# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
teams = ['England','Italy','Russia']
euro[euro['Team'].isin(teams)].loc[:,['Team','Shooting Accuracy']]
