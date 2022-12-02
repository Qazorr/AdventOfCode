calories = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        calories.append(line.strip())

overall = 0
output = []
for value in calories:
    if value != '':
        overall += int(value)
    else:
        output.append(overall)
        overall = 0
print(sorted(output)[-3:])
print(sum(sorted(output)[-3:]))
