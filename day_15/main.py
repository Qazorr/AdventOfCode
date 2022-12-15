from pprint import pprint

def parse(file):
    with open(file, 'r') as f:
        to_return = []
        lines = list(map(lambda x: x.strip().split(), f.readlines()))
        for line in lines:
            to_return.append([x[2:] for x in line if x[0] in ['x', 'y']])
        for i in range(len(to_return)):
            for j in range(4):
                to_return[i][j] = int(to_return[i][j][:-1]) if to_return[i][j][-1] in [',', ':'] else int(to_return[i][j])
    return to_return

manhattan = lambda p, q: (abs(p[0] - q[0]), abs(p[1] - q[1]))

def interpret(lines):
    for i in range(len(lines)):
        xS, yS, xB, yB = lines[i]
        S, B = (xS, yS), (xB, yB)
        lines[i] = [S, B, manhattan(S, B)]

y = 2_000_000
interpret(lines := parse('input.txt'))
rs = []
beacons = set()
for line in lines:
    S, B, diff = line
    if B[1] == y:
        beacons.add(B[0])
    ab = diff[0] + diff[1]
    dy = abs(S[1] - y)
    steps = ab - dy
    if steps > 0:
        rs.append(list(range(S[0]-steps, S[0]+steps+1)))

output = set()
for r in rs:
    output |= set(r)
output -= beacons
print(len(output))