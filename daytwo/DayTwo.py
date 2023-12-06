class DayTwoSolver:
    def __init__(self):
        pass

    def process_set(self, s):
        color_counts = {'red': 0, 'green': 0, 'blue': 0}
        s = s.split(',')
        for group in s:
            count, color = group.strip().split(' ')
            color_counts[color] += int(count)
        return color_counts

    def read_file(self, input_file):
        all_sets = []
        with open(input_file) as f:
            for line in f:
                game, info = line.strip().split(':')
                game_id = int(game.split(' ')[1])
                sets = info.split(';')
                sets = [self.process_set(s) for s in sets]
                all_sets.append((game_id, sets))
        return all_sets
    
    def solve_one(self, input_file):
        all_sets = self.read_file(input_file)
        res = 0
        for game_id, sets in all_sets:
            valid = True
            for s in sets:
                if s['red'] > 12 or s['green'] > 13 or s['blue'] > 14:
                    valid = False
            if valid: res += game_id
        print(f'Day Two Part One Solution: {res}')
        return res

    def solve_two(self, input_file):
        all_sets = self.read_file(input_file)
        res = 0
        for _, sets in all_sets:
            red_min, green_min, blue_min = 0, 0, 0
            for s in sets:
                red_min = max(red_min, s['red'])
                green_min = max(green_min, s['green'])
                blue_min = max(blue_min, s['blue'])
            res += red_min * green_min * blue_min
        print(f'Day Two Part Two Solution: {res}')
        return res

solver = DayTwoSolver()
solver.solve_one('adventofcode-day-2-input.txt')
solver.solve_two('adventofcode-day-2-input.txt')





        