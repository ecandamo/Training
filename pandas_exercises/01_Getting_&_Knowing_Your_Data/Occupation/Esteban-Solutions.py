# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
file = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
# Step 3. Assign it to a variable called users and use the 'user_id' as index
users = pd.read_table(file, sep='|',index_col='user_id')
# Step 4. See the first 25 entries
users.head(25)
# Step 5. See the last 10 entries
users.tail(10)
# Step 6. What is the number of observations in the dataset?
users.shape
# Step 7. What is the number of columns in the dataset?
users.columns.value_counts().sum()
# Step 8. Print the name of all the columns.
for col in users.columns:
    print(col)
# Step 9. How is the dataset indexed?
users.index
# Step 10. What is the data type of each column?
users.dtypes
# Step 11. Print only the occupation column
users[['occupation']].head()
# Step 12. How many different occupations are in this dataset?
users['occupation'].nunique()
# Step 13. What is the most frequent occupation?
users['occupation'].value_counts().sort_values(ascending=False).head(1)
# Step 14. Summarize the DataFrame.
users.info()
# Step 15. Summarize all the columns
# Step 16. Summarize only the occupation column
# Step 17. What is the mean age of users?
users['age'].mean()
# Step 18. What is the age with least occurrence?
users['age'].value_counts().sort_values(ascending=True)
