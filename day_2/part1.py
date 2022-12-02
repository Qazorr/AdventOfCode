def outcome(opponent, you):
    if you == 'X': you = 'A'
    if you == 'Y': you = 'B'
    if you == 'Z': you = 'C'
    
    if opponent == you: return 3
    if any([opponent == 'A' and you == 'C', opponent == 'B' and you == 'A', opponent == 'C' and you == 'B']):
        return 0
    return 6

if __name__ == "__main__":
    score = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line.strip()
            opponent, you = line.split()
            score += ord(you) - 87
            score += outcome(opponent, you)
    print(score)
