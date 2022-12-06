def get_marker(inp, marker_len = 4):
    for i in range(len(inp)-(marker_len-1)):
        information = set()
        for j in range(marker_len):
            information.add(inp[i+j])
        if(len(information) == marker_len):
            return i+marker_len
        
if __name__ == "__main__":    
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print(f'Part 1: {get_marker(line)}')
            print(f'Part 2: {get_marker(line, marker_len=14)}')