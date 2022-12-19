class Solution:
    def __init__(self, file='input.txt', max_width=7) -> None:
        self.top = 0
        self.shape = 0
        self.dropped = 0
        self.max_width = max_width
        self.positions = self.get_shape()
        self.rest = set([(i, 0) for i in range(self.max_width)])
        self.pattern_indicator = 0
        self.pattern = self.parse(file)

    def __str__(self) -> str:
        return self.positions.__str__()

    def parse(self, file):
        with open(file, 'r') as f:
            return [c for c in f.readline()]
            
    def pattern_interpret(self):
        direction = 'left' if self.pattern[self.pattern_indicator] == '<' else 'right'
        self.pattern_indicator = (self.pattern_indicator + 1) % (len(self.pattern))
        return direction
        
    def get_shape(self, starts=2):
        rock = []
        match self.shape:
            case 0:
                rock = [(starts+i, self.top+4) for i in range(4)]
            case 1:
                rock = [(starts+1, self.top+4+2)]
                rock.extend([(starts+i, self.top+4+1) for i in range(3)])
                rock.extend([(starts+1, self.top+4)])
            case 2:
                rock = [(starts+2, self.top+4+2-i) for i in range(2)]
                rock.extend([(starts+i, self.top+4) for i in range(3)])
            case 3:
                rock = [(starts, self.top+4+3-i) for i in range(4)]
            case 4:
                rock = [(starts+i, self.top+4+1-j) for j in range(2) for i in range(2)]
            case _:
                pass
        self.shape = (self.shape + 1) % 5
        return rock

    def move(self, dir):
        match dir:
            case 'left':
                if not any(((col <= 0) or ((col-1, row) in self.rest)) for col, row in self.positions):
                    self.positions = [(max(0, col-1), row) for col, row in self.positions]
            case 'right':
                if not any(((col >= self.max_width-1) or ((col+1, row) in self.rest)) for col, row in self.positions):
                    self.positions = [(min(self.max_width, col+1), row) for col, row in self.positions]
            case 'down':
                new_pos = [(col, row-1) for col, row in self.positions]
                if any(pos in self.rest for pos in new_pos):
                    self.rest |= set(self.positions)
                    self.top = max(self.top, max(new_pos, key=lambda x: x[1])[1] + 1) 
                    self.dropped += 1
                    self.positions = self.get_shape()
                else:
                    self.positions = new_pos
                    
    def solve(self, amount_dropped):
        while self.dropped != amount_dropped:
            if (self.dropped % (amount_dropped // 100) == 0):
                print(f'{self.dropped}/{amount_dropped}', end='\r')
            self.move(self.pattern_interpret())
            self.move('down')
        return self.top
    
    def show(self) -> None:
        for row in range(self.top+7, 0, -1):
            print('|', end='')
            for col in range(self.max_width):
                if (col, row) in self.positions:
                    print('@' if (col, row) in self.positions else '-', end=' ')
                else:
                    print('#' if (col, row) in self.rest else '-', end=' ')
            print('|')
        print(f'+{"-" * self.max_width}+')
        

part1, part2 = Solution('input.txt'), Solution('input.txt')
print(f'Part 1: {part1.solve(2022)}')
print(f'Part 2: {part1.solve(1000000000000)}')
