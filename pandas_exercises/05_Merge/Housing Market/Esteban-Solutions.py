# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Create 3 differents Series, each of length 100, as follows:
# 1. The first a random number from 1 to 4
rand1 = pd.Series(np.random.randint(low=1, high=5, size=100))
# 2. The second a random number from 1 to 3
rand2 = pd.Series(np.random.randint(low=1, high=4, size=100))
# 3. The third a random number from 10,000 to 30,000
rand3 = pd.Series(np.random.randint(low=10000, high=30001, size=100))
# Step 3. Let's create a DataFrame by joinning the Series by column
df = pd.DataFrame(pd.concat([rand1, rand2, rand3], axis=1))
# Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter
df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']
# Step 5. Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'
bigcolumn = pd.DataFrame(pd.concat([df.bedrs, df.bathrs, df.price_sqr_meter], axis = 0))
# Step 6. Oops, it seems it is going only until index 99. Is it true?
bigcolumn.index
# Step 7. Reindex the DataFrame so it goes from 0 to 299
bigcolumn = bigcolumn.reset_index(drop = True)
bigcolumn.index
