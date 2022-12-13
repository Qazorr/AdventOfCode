import re
from functools import cmp_to_key

islist = lambda x: isinstance(x, list)
isint = lambda x: isinstance(x, int)
        
def parse(file):
    with open(file, 'r') as f:
        lines = filter(lambda x: x != [''], list(map(lambda x: x.strip().split('\n\n'), f.readlines())))
    
    tmp = []
    for line in lines:
        if not re.match(r'[\[\]0-9,]*', line[0]): return
        tmp.append(eval(line[0]))
    return tmp

def compare(left, right):
    if isint(left) and isint(right):
        return -1 if left < right else 1 if left > right else 0
    if islist(left) and islist(right):
        for i in range(min(len(left), len(right))):
            cmp = compare(left[i], right[i])
            if cmp: return cmp
        return compare(len(left), len(right))
    if isint(left) and islist(right):
        return compare([left], right)
    if islist(left) and isint(right):
        return compare(left, [right])

if __name__ == "__main__":
    values = parse('input.txt')
    score = 0
    for i in range(0, len(values), 2):
        if compare(values[i], values[i+1]) <= 0:
            score += i//2+1
    print(f'Part 1: {score}')

    values.extend([[[2]], [[6]]])
    sorted_values = sorted(values, key=cmp_to_key(compare))
    idx_2 = sorted_values.index([[2]])
    idx_6 = sorted_values.index([[6]])
    print(f'Part 2: {(idx_2+1)*(idx_6+1)}')
