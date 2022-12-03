def priority(letter): return (ord(letter) - 96) + (58 if letter.isupper() else 0)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    compartments = []
    for line in lines:
        line = line.strip()
        mid = len(line)//2
        compartments.append((set(line[:mid]), set(line[mid:])))
    
priorities = 0
for left, right in compartments:
    for c in left:
        if c in right:
            priorities += priority(c)    
print(priorities)