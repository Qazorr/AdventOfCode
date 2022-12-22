from copy import copy

class Number:
    def __init__(self, value) -> None:
        self.value = int(value)

def parse(file):
    with open(file, 'r') as f:
        lines = list(map(lambda x: Number(x), f.readlines()))
        zero = next((x for x in lines if x.value == 0), None)
    return lines, copy(lines), zero

def mix(numbers, order):
    for o in order:
        number = numbers[numbers.index(o)]
        i = numbers.index(number)
        offset = abs(number.value) % (len(numbers) - 1)
        offset = -offset if number.value < 0 else offset
        position = i + offset
        if position >= len(numbers):
            position = (position + 1) % len(numbers)
        elif position == 0:
            position = 0 if offset >= 0 else len(numbers)
        numbers.insert(position, numbers.pop(i))


def get_score(numbers, zero, indexes=[1000, 2000, 3000]):
    score = 0
    zero_idx = numbers.index(zero)
    for i in indexes:
        idx = (zero_idx + (i % len(numbers))) % len(numbers)
        score += numbers[idx].value
    return score

def solve(numbers, order, zero, mixes=1, decryption_key=1):
    for number in numbers:
        number.value *= decryption_key
    for _ in range(mixes):
        mix(numbers, order)
    return get_score(numbers, zero)    

if __name__ == "__main__":
    p1 = solve(*parse('input.txt'))
    p2 = solve(*parse('input.txt'), mixes=10, decryption_key=811589153)
    print(f'Part 1: {p1}') 
    print(f'Part 2: {p2}')
