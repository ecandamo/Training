# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv).
file = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
# Step 3. Assign it to a variable called drinks.
drinks = pd.read_csv(file)
drinks.head()
# Step 4. Which continent drinks more beer on average?
drinks.groupby(['continent'])[['beer_servings']].agg('sum').sort_values(by='beer_servings', ascending=False).head(1)
# Step 5. For each continent print the statistics for wine consumption.
drinks.groupby(['continent'])[['wine_servings']].agg('describe')
# Step 6. Print the mean alcohol consumption per continent for every column
drinks.groupby(['continent'])[['total_litres_of_pure_alcohol']].agg('mean')
# Step 7. Print the median alcohol consumption per continent for every column
drinks.groupby(['continent'])[['total_litres_of_pure_alcohol']].agg('median')
# Step 8. Print the mean, min and max values for spirit consumption.
drinks[['spirit_servings']].agg(['mean','min','max'])
