def get_input(file):
    monkeys = {}
    with open(file, 'r') as f:
        lines = list(map(lambda x: x.strip().split(), f.readlines()))
        mod = 1
        for line in lines:
            if line:
                match line[0]:
                    case 'Monkey':
                        monkey = line[1][:-1]
                        monkeys[monkey] = {'activity': 0}
                    case 'Starting':
                        monkeys[monkey]['items'] = list(map(int, [num if num[-1] != ',' else num[:-1] for num in line[2:]]))
                    case 'Operation:':
                        monkeys[monkey]['operation'] = line[4:]
                    case 'Test:':
                        monkeys[monkey]['test'] = int(line[-1])
                        mod *= int(line[-1])
                    case 'If':
                        monkeys[monkey][line[1][:-1]] = line[-1]
        return monkeys, mod

def operation(op, worry):
    value = worry if op[1] == 'old' else int(op[1])
    match op[0]:
        case '*': return worry * value
        case '+': return worry + value
        case _: return 0

def test(test, worry):
    return worry % test == 0

def part1_round(monkeys):
    for monkey in monkeys.keys():
        monkeys[monkey]['activity'] += len(monkeys[monkey]['items'])
        for item in monkeys[monkey]['items']:
            worry_lvl = operation(monkeys[monkey]['operation'], item)
            worry_lvl //= 3
            passed = str(test(monkeys[monkey]['test'], worry_lvl)).lower()
            monkeys[monkeys[monkey][passed]]['items'].append(worry_lvl)
        monkeys[monkey]['items'].clear()

def part2_round(monkeys, mod):
    for monkey in monkeys.keys():
        monkeys[monkey]['activity'] += len(monkeys[monkey]['items'])
        for item in monkeys[monkey]['items']:
            worry_lvl = operation(monkeys[monkey]['operation'], item)            
            worry_lvl %= mod 
            passed = str(test(monkeys[monkey]['test'], worry_lvl)).lower()
            monkeys[monkeys[monkey][passed]]['items'].append(worry_lvl)
        monkeys[monkey]['items'].clear()


def get_activity(monkeys):
    return [monkeys[monkey]['activity'] for monkey in monkeys.keys()]

if __name__ == "__main__":
    monkeys, mod = get_input('input.txt')
    for _ in range(20):
        part1_round(monkeys)

    activity = get_activity(monkeys)
    first, second = sorted(activity)[-2:]
    print(f'Activity: {activity}')
    print(f'Part 1: {first*second}')
    
    monkeys, mod = get_input('input.txt')
    for _ in range(10000):
        part2_round(monkeys, mod)
    print()
    
    activity = get_activity(monkeys)
    first, second = sorted(activity)[-2:]
    print(f'Activity: {activity}')
    print(f'Part 2: {first*second}')
