import pandas as pd
import numpy as np

with open('AoC_2_Input.txt', 'r') as file:
    data = [line.strip().split() for line in file]

df = pd.DataFrame(data).apply(pd.to_numeric, errors='coerce').astype('float64')

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
