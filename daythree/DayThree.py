class DayThreeSolver:
    def __init__(self):
        self.dirs = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

    def read_file(self, file_name):
        grid = []
        with open(file_name, "r") as f:
            for line in f:
                grid.append([char for char in line.strip()])
        return grid
    
    def solve_one(self, file_name):
        res = 0
        grid = self.read_file(file_name)
        for i in range(len(grid)):
            j = 0
            while j < len(grid[0]):
                if grid[i][j].isdigit():
                    start, adjacent = j, False
                    while j < len(grid[0]) and grid[i][j].isdigit(): 
                        if not adjacent:
                            for di, dj in self.dirs:
                                new_i, new_j = i + di, j + dj
                                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                                    if not grid[new_i][new_j].isdigit() and grid[new_i][new_j] != ".":
                                        adjacent = True
                                        break
                        j += 1
                    num = int("".join(grid[i][start:j]))
                    if adjacent: res += num
                j += 1
        print(f'Day 3 Part 1: {res}')
        return res
    
    def solve_two(self, file_name):
        res = 0
        grid = self.read_file(file_name)
        # Get the indices of all part numbers, hash them to their corresponding number
        idx_to_part_num = {}
        for i in range(len(grid)):
            j = 0
            while j < len(grid[0]):
                if grid[i][j].isdigit():
                    start, adjacent = j, False
                    while j < len(grid[0]) and grid[i][j].isdigit():
                        if not adjacent:
                            for di, dj in self.dirs:
                                new_i, new_j = i + di, j + dj
                                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                                    if not grid[new_i][new_j].isdigit() and grid[new_i][new_j] != ".":
                                        adjacent = True
                                        break
                        j += 1
                    num = int("".join(grid[i][start:j]))
                    if adjacent:
                        for k in range(start, j): idx_to_part_num[(i, k)] = (num, i, start, j)
                j += 1

        # Loop through grid, if *, check if it adjacent to exactly two part numbers
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    adjacent = []
                    for di, dj in self.dirs:
                        new_i, new_j = i + di, j + dj
                        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                            if (new_i, new_j) in idx_to_part_num:
                                n, r, s, e = idx_to_part_num[(new_i, new_j)]
                                match = False
                                for n_, r_, s_, e_ in adjacent:
                                    if r_ == r and s_ == s and e_ == e:
                                        match = True
                                        break
                                if not match: adjacent.append((n, r, s, e))
                    if len(adjacent) == 2: res += adjacent[0][0] * adjacent[1][0]   
        
        print(f'Day 3 Part 2: {res}')
        return res
         



solver = DayThreeSolver()
solver.solve_one("day-3-sample.txt")
solver.solve_one("adventofcode-day-3-input.txt")
solver.solve_two("day-3-sample.txt")
solver.solve_two("adventofcode-day-3-input.txt")

                            

