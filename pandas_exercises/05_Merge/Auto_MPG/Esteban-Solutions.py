# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the first dataset [cars1](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv) and [cars2](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv).
cars1 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv'
cars2 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv'
# Step 3. Assign each to a variable called cars1 and cars2
cars1 = pd.read_csv(cars1)
cars2 = pd.read_csv(cars2)
# Step 4. Oops, it seems our first dataset has some unnamed blank columns, fix cars1
cars1 = cars1.dropna(axis=1)
# Step 5. What is the number of observations in each dataset?
cars1.shape
cars2.shape
# Step 6. Join cars1 and cars2 into a single DataFrame called cars
cars = pd.concat([cars1,cars2], axis=0)
# Step 7. Oops, there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.
owners = np.random.randint(low=15000, high=73001, size = len(cars.index))
# Step 8. Add the column owners to cars
cars['owners'] = owners
cars.head()
