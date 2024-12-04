import pandas as pd
import numpy as np

df = pd.read_excel('AoC_1.xlsx', header=None, sheet_name='CleanData')

location_one = np.sort(df[0].to_numpy())
location_two = np.sort(df[1].to_numpy())

distance = 0
for loc in range(location_one.size):
    distance += abs(location_one[loc] - location_two[loc])

print(distance)
