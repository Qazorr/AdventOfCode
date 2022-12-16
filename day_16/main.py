from random import choice, random
import copy


def parse(file):
    valves = {}
    with open(file, 'r') as f:
        lines = list(map(lambda x: x.strip().split(), f.readlines()))
        for line in lines:
            valves[line[1]] = {'opened': False}
            valves[line[1]]['flow-rate'] = int(line[4].split('=')[1][:-1])
            valves[line[1]]['lead-to'] = [tunnel[:-1] if tunnel[-1] == ',' else tunnel for tunnel in line[9:]]
    return valves

def interpret(valves):
    current, previous = 'AA', 'AA'
    pressure, time = 0, 30
    vvs = copy.deepcopy(valves)
    while(time >= 0):
        valve = vvs[current]
        if all([random() > 0.2, not valve['opened'], valve['flow-rate'] != 0]):
            time -= 1
            valve['opened'] = True
            pressure += time*valve['flow-rate']

        choices = valve['lead-to'][:]
        if all([random() > 0.1, previous in choices, len(choices) > 1]):
            choices.remove(previous)
        previous = current
        current = choice(choices)
        time -= 1
    return pressure

def try_valves(times):
    valves = parse('input.txt')
    pressure = 0
    for i in range(times):
        next_pressure = interpret(valves)
        if next_pressure > pressure:
            pressure = next_pressure
            print(f'{i}: {pressure}')

if __name__ == "__main__":
    try_valves(1_000_000)
    