# Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data
import pandas as pd
import numpy as np
file = '/Users/ecandamo/Documents/GitHub/Training/pandas_exercises/01_Getting_&_Knowing_Your_Data/World Food Facts/data.tsv'
# Step 2. Download the dataset to your computer and unzip it
# Step 3. Use the tsv file and assign it to a dataframe called food
data = pd.read_table(file, chunksize=5000)
# Step 4. See the first 5 entries
food = pd.DataFrame(data.get_chunk())
food.head(5)
# Step 5. What is the number of observations in the dataset?
food.shape
# Step 6. What is the number of columns in the dataset?
food.columns.value_counts().sum()
# Step 7. Print the name of all the columns.
food.columns
# Step 8. What is the name of 105th column?
food.columns[104]
# Step 9. What is the type of the observations of the 105th column?
food.iloc[:,104].dtype
# Step 10. How is the dataset indexed?
food.index
# Step 11. What is the product name of the 19th observation?
food.loc[18,'product_name']
