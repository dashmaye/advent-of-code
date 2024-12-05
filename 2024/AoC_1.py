import pandas as pd
import numpy as np

df = pd.read_excel('AoC_1.xlsx', header=None, sheet_name='CleanData')

location_one = np.sort(df[0].to_numpy())
location_two = np.sort(df[1].to_numpy())

# part one to get distance
distance = 0
for loc in range(location_one.size):
    distance += abs(location_one[loc] - location_two[loc])

print(distance)

# part two to get similarity
similarity = 0
for loc_a in range(location_one.size):
    occurence = 0
    for loca_b in range(location_one.size):
        if location_one[loc_a] == location_two[loca_b]:
            occurence += 1
    temp = location_one[loc_a] * occurence
    similarity += temp

print(similarity)
