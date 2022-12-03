def priority(letter): return (ord(letter) - 96) + (58 if letter.isupper() else 0)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    compartments = []
    for line in lines:
        compartments.append(set(line.strip()))

priorities = 0
for i in range(0, len(compartments), 3):
    badge = list(compartments[i] & compartments[i+1] & compartments[i+2])[0]
    priorities += priority(badge)
print(priorities)