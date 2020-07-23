# This time we are going to pull data directly from the internet.
# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv).
file = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# Step 3. Assign it to a variable called chipo.
chipo = pd.read_table(file)
# Step 4. How many products cost more than $10.00?
chipo['item_price'] = chipo['item_price'].str.replace('$','').astype(float)
chipo[chipo['item_price']>10].index.value_counts().sum()
# Step 5. What is the price of each item?
# Print a data frame with only two columns item_name and item_price
chipo[['item_name','item_price']].head()
# Step 6. Sort by the name of the item
chipo.sort_values(by='item_name').head()
# Step 7. What was the quantity of the most expensive item ordered?
chipo.sort_values(by='item_price', ascending = False).head(1).loc[:,'item_name']
# Step 8. How many times was a Veggie Salad Bowl ordered?
chipo[chipo['item_name'] == 'Veggie Salad Bowl'].loc[:,'quantity'].sum()
# Step 9. How many times did someone order more than one Canned Soda?
chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)].index.value_counts().sum()
