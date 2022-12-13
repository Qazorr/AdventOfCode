def parse(file):
    calories = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            calories.append(line.strip())
    return calories

def solve(calories):
    overall = 0
    calories_per_elf = []
    for value in calories:
        if value != '':
            overall += int(value)
        else:
            calories_per_elf.append(overall)
            overall = 0
    return calories_per_elf

if __name__ == "__main__":
    calories = solve(parse('input.txt'))
    print(f'Part 1: {max(calories)}')
    print(f'Part 2: {sum(sorted(calories)[-3:])}')
