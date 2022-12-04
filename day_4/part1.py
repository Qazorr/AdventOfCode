def subset_check(first_set, second_set): return (first_set[0] >= second_set[0]) and (first_set[1] <= second_set[1])

pairs = []
with open('input.txt', 'r') as f:
    lines = f.readlines()    
    for line in lines:
        line = line.strip().split(',')
        pairs.append((line[0], line[1]))
        
fully_contained = 0

for pair in pairs:
    first, second = tuple(map(int, pair[0].split('-'))), tuple(map(int, pair[1].split('-')))
    if subset_check(first, second) or subset_check(second, first):
        fully_contained += 1
        
print(fully_contained)