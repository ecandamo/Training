#Step 1. Import the necessary librariesimport numpy as np
import pandas as pd
import numpy as np
#Step 2. Import the dataset from this address.
file = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
#Step 3. Assign it to a variable called chipo.
chipo = pd.read_table(file)
#Step 4. See the first 10 entries
chipo.head(10)
#Step 5. What is the number of observations in the dataset?
chipo.shape
#Step 6. What is the number of columns in the dataset?
chipo.columns.value_counts().sum()
#Step 7. Print the name of all the columns.
chipo.columns
#Step 8. How is the dataset indexed?
chipo.index
#Step 9. Which was the most-ordered item?
chipo['item_name'].value_counts().sort_values(ascending = False).head(1)
#Step 10. For the most-ordered item, how many items were ordered?
chipo[chipo['item_name']=='Chicken Bowl'].loc[:,['item_name','quantity']].sum()
#Step 11. What was the most ordered item in the choice_description column?
chipo['choice_description'].value_counts().sort_values(ascending=False).head(1)
#Step 12. How many items were orderd in total?
chipo['quantity'].agg('sum')
#Step 13. Turn the item price into a float
#Step 13.a. Check the item price type
chipo['item_price'].dtype
#Step 13.b. Create a lambda function and change the type of item price
chipo['item_price'] = chipo['item_price'].str.replace('$','')
change_type = lambda x: pd.to_numeric(x)
chipo['item_price'] = chipo['item_price'].apply(change_type)
#Step 13.c. Check the item price type
chipo['item_price'].dtype
#Step 14. How much was the revenue for the period in the dataset?
chipo['revenue'] = chipo['quantity']*chipo['item_price']
chipo['revenue'].sum()
#Step 15. How many orders were made in the period?
chipo['order_id'].nunique()
#Step 16. What is the average revenue amount per order?
chipo.groupby('order_id')[['revenue']].agg('mean')
#Step 17. How many different items are sold?
chipo['item_name'].nunique()
