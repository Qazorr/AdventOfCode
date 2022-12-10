import re

def get_input(file):
    with open(file, 'r') as f:
        return f.read().split()

def part1(inp):
    X, signal_strenghts =  1, []
    for cycle_no, value in enumerate(inp, start=1):
        if cycle_no % 40 == 20: signal_strenghts.append(X * cycle_no)
        if value.lstrip("-").isnumeric(): X += int(value)
    return sum(signal_strenghts)

def part2(inp):
    X, image = 1, ''
    for cycle_no, value in enumerate(inp, start=1):
        if abs((cycle_no-1) % 40 - X) < 2: image += '#'
        else: image += ' '
        if value.lstrip("-").isnumeric(): X += int(value)

    # add newline every 40 characters so the image can be read
    return re.sub("(.{40})", "\\1\n", image, 0, re.DOTALL)


lines = get_input('input.txt')
print(part1(lines))
print(part2(lines))
