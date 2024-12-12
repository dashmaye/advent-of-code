import re

full_list = []
with open('../Data_Inputs/AoC_4_input.txt', 'r') as file:
    for line in file:
        full_list.append(line)

# part one getting all instances of XMAS
xmas = re.compile("(?=(XMAS|SAMX))")
xmas_matches = []

for line in full_list:
    xmas_matches.extend(xmas.findall(line))

xmas_count = len(xmas_matches)

for i in range(0, len(full_list) - 3):
    x = full_list[i]
    m = full_list[i + 1]
    a = full_list[i + 2]
    s = full_list[i + 3]

    for j in range(len(x)):
        # vertical matches, top-down
        if x[j] == "X" and m[j] == "M" and a[j] == "A" and s[j] == "S":
            xmas_count += 1

        # vertical matches, bottom-up
        if x[j] == "S" and m[j] == "A" and a[j] == "M" and s[j] == "X":
            xmas_count += 1

    for k in range(len(x) - 3):

        # diagonal matches, top-down, left-to-right
        if x[k] == "X" and m[k + 1] == "M" and a[k + 2] == "A" and s[k + 3] == "S":
            xmas_count += 1

        # diagonal matches, top-down, right-to-left
        if x[k + 3] == "X" and m[k + 2] == "M" and a[k + 1] == "A" and s[k] == "S":
            xmas_count += 1

        # diagonal matches, bottom-up, left-to-right
        if x[k] == "S" and m[k + 1] == "A" and a[k + 2] == "M" and s[k + 3] == "X":
            xmas_count += 1

        # diagonal matches, bottom-up, right-to-left
        if x[k + 3] == "S" and m[k + 2] == "A" and a[k + 1] == "M" and s[k] == "X":
            xmas_count += 1

print(len(xmas_count))

# part two getting all instances of x-mas
xmas_count = 0
for i in range(0, len(full_list) - 2):
    x = full_list[i]
    m = full_list[i + 1]
    a = full_list[i + 2]

    for j in range(len(x) - 2):
        if x[j] == "M" and x[j + 2] == "M" and m[j + 1] == "A" and a[j] == "S" and a[j + 2] == "S":
            xmas_count += 1
        if x[j] == "M" and x[j + 2] == "S" and m[j + 1] == "A" and a[j] == "M" and a[j + 2] == "S":
            xmas_count += 1
        if x[j] == "S" and x[j + 2] == "M" and m[j + 1] == "A" and a[j] == "S" and a[j + 2] == "M":
            xmas_count += 1
        if x[j] == "S" and x[j + 2] == "S" and m[j + 1] == "A" and a[j] == "M" and a[j + 2] == "M":
            xmas_count += 1

print(xmas_count)