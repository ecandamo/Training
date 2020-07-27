# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv).
file = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
# Step 3. Assign it to a variable called baby_names.
baby_names = pd.read_csv(file)
# Step 4. See the first 10 entries
baby_names.head(10)
# Step 5. Delete the column 'Unnamed: 0' and 'Id'
baby_names = baby_names.drop(baby_names.columns[0],axis=1)
# Step 6. Is there more male or female names in the dataset?
baby_names['Gender'].value_counts()
# Step 7. Group the dataset by name and assign to names
names = baby_names.groupby('Name')[['Count']].agg('sum')
# Step 8. How many different names exist in the dataset?
baby_names['Name'].nunique()
names.index.value_counts().sum()
# Step 9. What is the name with most occurrences?
names.sort_values(by ='Count', ascending=False)
# Step 10. How many different names have the least occurrences?
names[names['Count'] == names.sort_values(by ='Count', ascending=False).iloc[-1,-1]].shape[0]
# Step 11. What is the median name occurrence?
names.agg('median')
# Step 12. What is the standard deviation of names?
names.agg('std')
# Step 13. Get a summary with the mean, min, max, std and quartiles.
names.agg(['mean','min','max','std'])
