SNAFU = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

def parse(file):
    with open(file, 'r') as f:
        return f.read().splitlines()
 
def snafu2dec(snafu: str):
    dec, power = 0, 5**len(snafu)
    for num in snafu:
        power //= 5
        dec += power * SNAFU[num]
    return dec
    
def dec2snafu(dec: int):
    if not dec: return ''
    match dec % 5:
        case 0 | 1 | 2:
            return dec2snafu(dec//5) + str(dec % 5)
        case 3:
            return dec2snafu(1 + dec//5) + '='
        case 4:
            return dec2snafu(1 + dec//5) + '-'

p1 = dec2snafu(sum(snafu2dec(num) for num in parse('input.txt')))
print(f'Part 1: {p1}')