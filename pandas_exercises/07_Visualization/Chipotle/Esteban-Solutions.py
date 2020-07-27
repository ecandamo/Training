# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
# set this so the graphs open internally
%matplotlib inline
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv).
file = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# Step 3. Assign it to a variable called chipo.
chipo = pd.read_table(file)
# Step 4. See the first 10 entries
chipo.head(10)
# Step 5. Create a histogram of the top 5 items bought
top5 = chipo.groupby(['item_name'])['quantity'].sum().sort_values(ascending=False).head(5)
plt.bar(x=top5.index, height = top5.values)
# Step 6. Create a scatterplot with the number of items orderered per order price

# Step 7. BONUS: Create a question and a graph to answer your own question.
