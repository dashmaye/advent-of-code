import re

pattern = r"mul\((\d+),(\d+)\)"

matches = []

with open('../Data_Inputs/AoC_3_input.txt', 'r') as file:
    for line in file:
        # matches.extend(re.findall(pattern, line))
        matches.extend(re.findall(pattern, line))

# part one to get sumproduct
sum = 0
for x, y in matches:
    sum += (int(x) * int(y))

print(sum)

