def outcome(opponent, you):
    if you == 'X': 
        if opponent == 'A': return 'Z'
        if opponent == 'B': return 'X'
        if opponent == 'C': return 'Y'
    if you == 'Y': 
        if opponent == 'A': return 'X'
        if opponent == 'B': return 'Y'
        if opponent == 'C': return 'Z'
    if you == 'Z': 
        if opponent == 'A': return 'Y'
        if opponent == 'B': return 'Z'
        if opponent == 'C': return 'X'

if __name__ == "__main__":
    score = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line.strip()
            opponent, you = line.split()
            score += (ord(you) - 88) * 3
            score += ord(outcome(opponent, you)) - 87
    print(score)
