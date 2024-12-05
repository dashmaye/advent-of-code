import pandas as pd
import numpy as np

with open('AoC_2_Input.txt', 'r') as file:
    data = [line.strip().split() for line in file]

df = pd.DataFrame(data).apply(pd.to_numeric, errors='coerce').astype('float64')

# part one to find safe
safe = 0
for value in range(len(df)):
    row = df.iloc[value][pd.notna(df.iloc[value])].to_numpy()
    if all(df.iloc[value][i] < df.iloc[value][i + 1] for i in range(len(row) - 1)):
        if all(0 < abs(df.iloc[value][i] - df.iloc[value][i + 1]) <= 3 for i in range(len(row) - 1)):
            safe += 1
    elif all(df.iloc[value][i] > df.iloc[value][i + 1] for i in range(len(row) - 1)):
        if all(0 < abs(df.iloc[value][i] - df.iloc[value][i + 1]) <= 3 for i in range(len(row) - 1)):
            safe += 1
print(safe)

# part two to find dampened safe
damped = 0
for value in range(len(df)):
    row = df.iloc[value][pd.notna(df.iloc[value])].to_numpy()
    for i in range(len(row)):
        temp_row = np.delete(row, i)
        if (all(temp_row[j] < temp_row[j + 1] for j in range(len(temp_row) - 1)) and
            all(0 < abs(temp_row[j] - temp_row[j + 1]) <= 3 for j in range(len(temp_row) - 1))):
            damped += 1
            break
    
        if (all(temp_row[j] > temp_row[j + 1] for j in range(len(temp_row) - 1)) and
            all(0 < abs(temp_row[j] - temp_row[j + 1]) <= 3 for j in range(len(temp_row) - 1))):
            damped += 1
            break
print(damped)
