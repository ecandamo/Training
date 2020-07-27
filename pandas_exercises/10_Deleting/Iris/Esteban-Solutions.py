# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data).
file = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Step 3. Assign it to a variable called iris
iris = pd.read_table(file, sep=',', header=None)
# Step 4. Create columns for the dataset
# 1. sepal_length (in cm)
# 2. sepal_width (in cm)
# 3. petal_length (in cm)
# 4. petal_width (in cm)
# 5. class
cols = ['sepal_length','sepal_width', 'petal_lenght', 'petal_width', 'class']
# Step 5.  Is there any missing value in the dataframe?
iris.columns = cols
iris.head()
# Step 6.  Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN
iris.loc[10:29,'petal_lenght'] = np.NaN
# Step 7. Good, now lets substitute the NaN values to 1.0
iris = iris.fillna(1.0)
# Step 8. Now let's delete the column class
iris = iris.drop('class', axis=1)
# Step 9.  Set the first 3 rows as NaN
iris.iloc[:3] = np.NaN
# Step 10.  Delete the rows that have NaN
iris = iris.dropna(axis=0)
# Step 11. Reset the index so it begins with 0 again
iris = iris.reset_index(drop=True)
