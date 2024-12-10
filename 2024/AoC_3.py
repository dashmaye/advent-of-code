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


# part two to get sumproduct between do() & don't()
init_pattern = re.compile(".*?(do\(\).*?don't\(\)|don't\(\))")
pattern = re.compile("(?<=do\(\))(.*?)(?=don't\(\))")
mul_pattern = re.compile("mul\((\d+),(\d+)\)")

matches = []
mul_matches = []
first_line = True
full_string = ""

with open('../Data_Inputs/AoC_3_input.txt', 'r') as file:
    full_string = ''.join(line.strip() for line in file)

if first_line:
    init = init_pattern.search(full_string)
    mul_matches.extend(mul_pattern.findall(init.group(0)))
    first_line = False
matches.extend(pattern.findall(full_string))

for match in matches:
    mul_matches.extend(mul_pattern.findall(match))

sum = 0
for x, y in mul_matches:
    sum += (int(x) * int(y))

print(sum)