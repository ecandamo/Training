# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv).
file = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
# Step 3. Assign it to a variable called df.
df = pd.read_csv(file)
# Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
df = df.loc[:,'school':'guardian']
# Step 5. Create a lambda function that will capitalize strings.
df.head()
cap = lambda x: x.capitalize()
# Step 6. Capitalize both Mjob and Fjob
df['Mjob'] = df.loc[:,['Mjob']].applymap(cap)
df['Fjob'] = df.loc[:,['Fjob']].applymap(cap)
# Step 7. Print the last elements of the data set.
df.tail()
# Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
# Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority(x):
    return True if x > 17 else False

df['legal_drinker'] = df['age'].apply(majority)
# Step 10. Multiply every number of the dataset by 10.
def by_10(x):
    return x*10 if x.dtype == int else x

df.apply(by_10)     
