class DaySixSolver:
    def load_file(self, file_name, part=1):
        times, distances = [], []
        with open(file_name) as f:
            for line in f:
                l = line.strip()
                if l.find('Time') != -1:
                    if part == 1:
                        times.extend(int(val) for val in l.split()[1:])
                    elif part == 2:
                        times.append(int("".join(l.split()[1:])))
                if l.find('Distance') != -1:
                    if part == 1:
                        distances.extend(int(val) for val in l.split()[1:])
                    elif part == 2:
                        distances.append(int("".join(l.split()[1:])))
        return times, distances
    
    
    def solve(self, file_name, part=1):
        times, distances = self.load_file(file_name, part=part)
        res = 1
        for t, d in zip(times, distances):
            ways = 0
            for i in range(t):
                if i * (t - i) > d:
                    ways += 1
            res *= ways
        print(f"Day 6, part {part}: {res}")
        return res

solver = DaySixSolver()
solver.solve('adventofcode-day-6-input.txt', part=1)
solver.solve('adventofcode-day-6-input.txt', part=2)
