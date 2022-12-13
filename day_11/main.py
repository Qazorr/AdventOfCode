def parse(file):
    with open(file, 'r') as f:
        lines = list(map(lambda x: x.strip().split(), f.readlines()))
    monkeys = {}
    mod = 1
    for line in lines:
        if line:
            match line[0]:
                case 'Monkey':
                    monkey = line[1][:-1]
                    monkeys[monkey] = {'activity': 0}
                case 'Starting':
                    monkeys[monkey]['items'] = list(
                        map(int, [num if num[-1] != ',' else num[:-1] for num in line[2:]]))
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

def test(test, worry): return worry % test == 0

def round(monkeys, decrease_worry_lvl):
    for monkey in monkeys.keys():
        monkeys[monkey]['activity'] += len(monkeys[monkey]['items'])
        for item in monkeys[monkey]['items']:
            worry_lvl = operation(monkeys[monkey]['operation'], item)
            worry_lvl = decrease_worry_lvl(worry_lvl)
            passed = str(test(monkeys[monkey]['test'], worry_lvl)).lower()
            monkeys[monkeys[monkey][passed]]['items'].append(worry_lvl)
        monkeys[monkey]['items'].clear()


def monkey_business(monkeys):
    activity = [monkeys[monkey]['activity'] for monkey in monkeys.keys()]
    first, second = sorted(activity)[-2:]
    return activity, first*second

if __name__ == "__main__":
    monkeys, _ = parse('input.txt')
    for _ in range(20):
        round(monkeys, lambda x: x//3)
    _, score = monkey_business(monkeys)
    print(f'Part 1: {score}')

    monkeys, mod = parse('input.txt')
    for _ in range(10000):
        round(monkeys, lambda x: x % mod)
    _, score = monkey_business(monkeys)
    print(f'Part 2: {score}')
