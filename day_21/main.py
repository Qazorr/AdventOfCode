def parse(file):
    monkeys = {}
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().split(': ')
        monkeys[line[0]] = line[1].split()
    return monkeys

def part1(monkeys, monkey='root'):
    if len(monkeys[monkey]) == 1:
        return int(monkeys[monkey][0])
    m1, op, m2 = monkeys[monkey]        
    return int(eval(f'{part1(monkeys, m1)}{op}{part1(monkeys, m2)}'))

def part2(monkeys, monkey='root'):
    if len(monkeys[monkey]) == 1:
        return monkeys[monkey][0]
    m1, op, m2 = monkeys[monkey]
    return f'({part2(monkeys, m1)}{op}{part2(monkeys, m2)})'

if __name__ == "__main__":
    monkeys = parse('input.txt')
    monkeys['root'] = part1(monkeys)
    p1 = monkeys['root']
    print(f'Part 1: {p1}')
    
    # idea from: https://www.reddit.com/r/adventofcode/comments/zrav4h/comment/j133ko6/
    monkeys = parse('input.txt')
    monkeys['humn'], monkeys['root'][1] = ["-1j"], '-('
    p2 = eval(f'{part2(monkeys)})')
    print(f'Part 2: {int(p2.real / p2.imag)}')