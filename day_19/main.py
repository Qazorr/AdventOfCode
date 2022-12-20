from random import random
import itertools

def parse(file):
    blueprints = {}
    with open(file, 'r') as f:
        lines = f.readlines()
    curr = ''
    for line in lines:
        line = line.strip()[:-1].split()
        if not line: continue
        if line[0] == 'Blueprint':
            curr = line[1]
            blueprints[curr] = {}
        else:
            match line[1]:
                case 'ore' | 'clay':
                    blueprints[curr][line[1]] = {line[-1]: int(line[-2])}
                case 'obsidian' | 'geode':
                    el = [tuple(x.split()) for x in ' '.join(line[4:]).split('and')]
                    blueprints[curr][line[1]] = {}
                    for value, resource in el:
                        blueprints[curr][line[1]][resource] = int(value)
    return blueprints

def create_robot(blueprint, resources):
    robots = {
        'ore': 0,
        'clay': 0,
        'obsidian': 0,
        'geode': 0
    }
    
    if random() > 0.1 and all(resources[resource] >= blueprint['geode'][resource] for resource in ['ore', 'obsidian']):
        resources['ore'] -= blueprint['geode']['ore']
        resources['obsidian'] -= blueprint['geode']['obsidian']
        robots['geode'] += 1
    elif random() > 0.2 and all(resources[resource] >= blueprint['obsidian'][resource] for resource in ['ore', 'clay']):
        resources['ore'] -= blueprint['obsidian']['ore']
        resources['clay'] -= blueprint['obsidian']['clay']
        robots['obsidian'] += 1
    elif random() > 0.3 and resources['ore'] >= blueprint['clay']['ore']:
        resources['ore'] -= blueprint['clay']['ore']
        robots['clay'] += 1
    elif random() > 0.9 and resources['ore'] >= blueprint['ore']['ore']:
        resources['ore'] -= blueprint['ore']['ore']
        robots['ore'] += 1
    
    return robots


def run(blueprint, minutes, tries=1_000_000):
    score = 0
    for i in range(tries):
        resources = {
            'ore': 0,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }
        robots = {
            'ore': 1,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }
        for _ in range(minutes):
            new_robots = create_robot(blueprint, resources)
            for key, value in robots.items():
                resources[key] += value
            for key in new_robots.keys():
                robots[key] += new_robots[key]
        if resources['geode'] > score:
            score = max(score, resources['geode'])
            print(f'[{i}]: {score}')
    return score 

def part1(blueprints):
    score = 0
    for key, blueprint in blueprints.items():
        print(f'Working on {key}')
        score += run(blueprint, minutes=24) * int(key)
    print(f'\nPart 1: {score}\n')
    
def part2(blueprints):
    score = 1
    for key, blueprint in blueprints.items():
        print(f'Working on {key}')
        score *= run(blueprint, minutes=32)
    print(f'\nPart 2: {score}\n')

if __name__ == "__main__":
    blueprints = parse('input.txt')
    part1(blueprints)
    part2(dict(itertools.islice(parse('input.txt').items(), 3)))