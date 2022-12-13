def subset_check(first_set, second_set): return (first_set[0] >= second_set[0]) and (first_set[1] <= second_set[1])
def contain_check(first_set, second_set): return (first_set[0] <= second_set[0] <= first_set[1])

def parse(file):
    pairs = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            pairs.append((line[0], line[1]))
    return pairs

def solve(pairs, check):
    passed = 0
    for pair in pairs:
        first, second = tuple(map(int, pair[0].split('-'))), tuple(map(int, pair[1].split('-')))
        if check(first, second) or check(second, first):
            passed += 1
    return passed

print(solve(parse('input.txt'), subset_check))
print(solve(parse('input.txt'), contain_check))