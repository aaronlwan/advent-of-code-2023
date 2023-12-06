class DayOneSolver:
    def __init__(self):
        self.num_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def solve(self, input_file, part='One'):
        res = 0
        with open(input_file) as f:
            for line in f:
                num, digit, l = None, None, line.strip()
                for i, c in enumerate(l):
                    if c.isdigit():
                        digit = c
                    if part == 'Two':
                        for j in range(3, 6):
                            if i + j < len(l) + 1 and l[i:i+j] in self.num_strings:
                                digit = self.num_strings.index(l[i:i+j]) + 1
                    if num is None and digit: num = int(digit)
                num = 10 * num + int(digit)
                res += num
        print(f'Day One Part {part} Solution: {res}')
        return res

solver = DayOneSolver()
solver.solve('adventofcode-day-1-input.txt')
solver.solve('adventofcode-day-1-input.txt', part='Two')