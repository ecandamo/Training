# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
file = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
# Step 3. Assign it to a variable called users.
users = pd.read_table(file, sep = '|')
users.head()
# Step 4. Discover what is the mean age per occupation
users.groupby(['occupation'])[['age']].agg('mean').head()
# Step 5. Discover the Male ratio per occupation and sort it from the most to the least
users[users['gender']=='M'].groupby(['occupation'])['gender'].agg('count').sort_values(ascending=False)
# Step 6. For each occupation, calculate the minimum and maximum ages
users.groupby(['occupation'])['age'].agg(['min','max'])
# Step 7. For each combination of occupation and gender, calculate the mean age
users.groupby(['occupation','gender'])['age'].agg(['mean'])
# Step 8.  For each occupation present the percentage of women and men
male_occupation = users[users['gender'] == 'M'].groupby('occupation')['gender'].agg('count')
female_occupation = users[users['gender'] == 'F'].groupby('occupation')['gender'].agg('count')
total = pd.DataFrame(pd.concat([male_occupation,female_occupation], axis = 1))
total.columns = ['Male', 'Female']
total = total.fillna(0)
total['Male%'] = total['Male']/(total['Male']+total['Female'])*100
total['Female%'] = total['Female']/(total['Male']+total['Female'])*100
total.drop(['Male','Female'],axis=1)
