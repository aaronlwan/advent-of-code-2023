class DayFourSolver:
    def __init__(self):
        pass

    def solve_one(self, file_name):
        res = 0
        for winning_nums, your_nums in self.read_file(file_name):
                winners = 0
                for num in your_nums:
                    if num in winning_nums:
                        winners += 1
                res += 2 ** (winners - 1) if winners > 0 else 0
        print(f'Day 4 Part 1: {res}')
        return res
    

    def solve_two(self, file_name):
        res = 0
        data = self.read_file(file_name)
        copies = [1 for _ in range(len(data))]
        for i, (winning_nums, your_nums) in enumerate(data):
            winners = 0
            for num in your_nums:
                if num in winning_nums:
                    winners += 1
            if winners > 0:
                for j in range(1, winners + 1):
                    copies[j + i] += copies[i]
        res = sum(copies)
        print(f'Day 4 Part 2: {res}')
        return res

    def read_file(self, file_name):
        data = []
        with open(file_name) as f:
            lines = f.readlines()
            for line in lines:
                card, info = line.split(":")
                winning_nums, your_nums = info.split("|")
                winning_nums = [int(num) for num in winning_nums.strip().split()]
                your_nums = [int(num) for num in your_nums.strip().split()]
                data.append((winning_nums, your_nums))
        return data

solver = DayFourSolver()
solver.solve_one("day-4-sample.txt")
solver.solve_one("adventofcode-day-4-input.txt")
solver.solve_two("day-4-sample.txt")
solver.solve_two("adventofcode-day-4-input.txt")
