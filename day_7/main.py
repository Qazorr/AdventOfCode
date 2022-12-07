from collections import defaultdict

def get_input(file):
    with open(file, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))

def interpret(lines):
    files = defaultdict(list)
    dirs = ['']
    for line in lines:
        parts = line.split()
        actual_path = dirs[-1]
        if parts[0] == '$':
            match parts[1]:
                case 'cd':
                    if parts[2] == '..':
                        actual_path = '/'.join(actual_path.split('/')[:-2]) + '/'
                    elif parts[2] == '/':
                        actual_path = '/'
                    else:
                        actual_path += f'{parts[2]}/'
                    dirs.append(actual_path)
                case 'ls':
                    dir = actual_path[:-1] if actual_path != '/' else '/'
                case _:
                    pass
        else:
            if parts[0] == 'dir':
                parts[1] = actual_path+parts[1]
            else:
                parts.insert(0, 'file')
                parts[1], parts[2] = parts[2], parts[1]
            files[dir].append(parts)
    for key, value in files.items():
        files[key] = sorted(value, key=lambda x: x[0] == 'dir', reverse=True)
    return dirs[1:], files

def shallow_evaluation(files):
    for key, val in files.items():
        size = 0
        for element in val:
            if element[0] != 'dir':
                size += int(element[2])
        files[key].append(['size', size])

def recursive_evaluation(files, key):
    for element in files[key]:
        if element[0] == 'dir':
            files[key][-1][1] += recursive_evaluation(files, element[1])
    return files[key][-1][1]
    
def get_sizes(files):
    dir_sizes = {}
    for key, val in files.items():
        dir_sizes[key] = val[-1][1]
    return dir_sizes
    
def find_dir_to_delete(files, available, need):
    space_left = available - files['/'][-1][1]
    return sorted(
        list(filter(lambda x: x[1] > abs(need-space_left), get_sizes(files).items())), 
        key=lambda x: x[1]
    )[0]

def evaluate_sizes(files):
    shallow_evaluation(files)  # only looking at the files
    recursive_evaluation(files, '/')  # looking inside dirs
    
if __name__ == "__main__":        
    available, required = 70000000, 30000000
    _, files = interpret(get_input('input.txt'))
    evaluate_sizes(files)
    print(f"Part 1: {sum(x[1] for x in list(filter(lambda x: x[1] < 100000, get_sizes(files).items())))}")
    print(f"Part 2: {find_dir_to_delete(files, available, required)[1]}")