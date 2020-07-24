# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Create the DataFrame with the following values:
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
# Step 3. Assign it to a variable called regiment.
regiment = pd.DataFrame(raw_data, columns=raw_data.keys())
# Step 4. What is the mean preTestScore from the regiment Nighthawks?
regiment.groupby(['regiment'])[['preTestScore']].agg('mean').loc['Nighthawks',:]
# Step 5. Present general statistics by company
regiment.groupby('company').describe()
# Step 6. What is the mean of each company's preTestScore?
regiment.groupby('company')[['preTestScore']].agg('mean')
# Step 7. Present the mean preTestScores grouped by regiment and company
regiment.groupby(['regiment', 'company'])[['preTestScore']].agg('mean')
# Step 8. Present the mean preTestScores grouped by regiment and company without heirarchical indexing
regiment.groupby(['regiment', 'company'], as_index=False,)[['preTestScore']].agg('mean')

# Step 9. Group the entire dataframe by regiment and company
regiment.groupby(['regiment', 'company'])
# Step 10. What is the number of observations in each regiment and company
regiment.groupby(['regiment', 'company']).agg(['count'])
# Step 11. Iterate over a group and print the name and the whole data from the regiment
for n1 in regiment.groupby('regiment'):
    print(n1)
