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

def part1(valves):
    current, previous = 'AA', 'AA'
    pressure, time = 0, 30
    vvs = copy.deepcopy(valves)
    while(time >= 0):
        valve = vvs[current]
        
        # 80% chance of opening a valve if not opened and it's flowrate is not 0
        if all([random() > 0.2, not valve['opened'], valve['flow-rate'] != 0]): 
            time -= 1
            valve['opened'] = True
            pressure += time*valve['flow-rate']

        choices = valve['lead-to'][:]
        # 90% chance of not going back to the same spot as previous one if we have another path
        if all([random() > 0.1, previous in choices, len(choices) > 1]):
            choices.remove(previous)
        previous = current
        current = choice(choices)
        time -= 1
    return pressure

def part2(valves):
    current, previous = ['AA', 'AA'], ['AA', 'AA']
    pressure, time = 0, 26
    vvs = copy.deepcopy(valves)
    while (time >= 0):
        for i in range(2): # 0 - me, 1 - elephant
            valve = vvs[current[i]]
            if all([random() > 0.2, not valve['opened'], valve['flow-rate'] != 0]):
                valve['opened'] = True
                pressure += max(0, time-1)*valve['flow-rate']
            else:
                choices = valve['lead-to'][:]
                if all([random() > 0.1, previous[i] in choices, len(choices) > 1]):
                    choices.remove(previous[i]) # going back after making a move
                if all([random() > 0.2, current[0] in choices, len(choices) > 1, i == 1]):
                    choices.remove(current[0]) # elephant not going to the same spot as me
                previous[i] = current[i]
                current[i] = choice(choices)
        time -= 1
    return pressure

def solve(valves, times, part):
    pressure = 0
    for i in range(times):
        next_pressure = part(valves)
        if i % (times // 100):
            print(f'Loop done: {round((i/times)*100, 2)}%', end='\r')
        if next_pressure > pressure:
            pressure = next_pressure
            print(f'At {i} found new: {pressure}')

if __name__ == "__main__":
    solve(parse('input.txt'), 1_000_000, part2)
    