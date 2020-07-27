# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
# Step 2. Create a data dictionary that looks like the DataFrame below
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'], "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'], "type": ['grass', 'fire', 'water', 'bug'], "hp": [45, 39, 44, 45], "pokedex": ['yes', 'no', 'yes', 'no']}
# Step 3. Assign it to a variable called pokemon
pokemon = pd.DataFrame(raw_data)
# Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place  the order of the columns as name, type, hp, evolution, pokedex
pokemon.columns = ['name','type', 'hp', 'evolution', 'pokedex']
# Step 5. Add another column called place, and insert what you have in mind.
pokemon['place'] = 'Pallet Town'
# Step 6. Present the type of each column
pokemon.dtypes
