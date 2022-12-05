with open('input.txt', 'r') as f:
    lines = f.readlines()

# find end of the stack definiton in input
for stackend in range(len(lines)):
    if all(c.isnumeric() for c in lines[stackend].split()):
        break

# get the last index of the stack from the input
no_stacks = int(lines[stackend][-3])

# based on index of the letter put in in corresponding stack
stacks = [[] for _ in range(no_stacks)]
for line in range(stackend):
    for i, c in enumerate(lines[line]):
        if (i-1) % 4 == 0:
            if c != ' ':
                stacks[i // 4].append(c)

# reverse the lists so that we have a proper stack
stacks = [stack[::-1] for stack in stacks]

# for every operation in the input (move x from y to z)
for i in range(stackend+2, len(lines)):
    x, y, z = list(
        map(int, [num for num in lines[i].split()][1::2])  # get x,y,z
    )

    # get the beggining index of the added stack on top
    before = len(stacks[z-1])

    for j in range(x):
        if stacks[y-1]:
            stacks[z-1].append(stacks[y-1].pop())  # same as in part 1

    # get the ending index of the added stack on top
    after = len(stacks[z-1])

    # reverse the added part to preserve the order
    stacks[z-1][before:after] = list(reversed(stacks[z-1][before:after]))

# print top of the stack of every stack
print(''.join(list(stack[-1] for stack in stacks)))
