from collections import defaultdict, deque
from tqdm import tqdm

class DayFiveSolver:
    def read_file(self, file_path, part=1):
        seeds, maps = [], defaultdict(dict)
        curr_key = None
        with open(file_path, "r") as f:
            for line in f.readlines():
                l = line.strip()
                if l.find('seeds') != -1:
                    if part == 1:
                        seeds = l.split(':')[1].strip().split()
                    elif part == 2:
                        parsed = l.split(':')[1].strip().split()
                        seeds = []
                        for i in range(0, len(parsed), 2):
                            seeds.append((int(parsed[i]), int(parsed[i]) + int(parsed[i + 1]) - 1))
                elif l.find('map') != -1:
                    source, _, dest = l.split()[0].split('-')
                    curr_key = (source, dest)
                elif len(l) > 0:
                    dest_start, source_start, rng = l.split()
                    maps[curr_key][(int(source_start), int(rng))] = int(dest_start)
        return seeds, maps
    
    def solve_one(self, file_path):
        res = float('inf')
        seeds, maps = self.read_file(file_path)
        for seed in seeds:
            source, source_val = 'seed', int(seed)
            while True:
                for src, dst in maps.keys():
                    if src == source: map, dest = maps[(src, dst)], dst
                dest_val = self.convert(source_val, map)
                if dest == 'location':
                    res = min(res, dest_val)
                    break

                source, source_val = dest, dest_val
        print(f'Day 5 Part 1: {res}')
        return res
    
    def solve_two(self, file_path):
        res = float('inf')
        seeds, maps = self.read_file(file_path, part=2)
        q = deque([('seed', start, end) for start, end in seeds])
        while q:
            source, source_start, source_end = q.pop()
            if source == 'location':
                res = min(res, source_start)
                continue
            for src, dst in maps.keys():
                if src == source: map, dest = maps[(src, dst)], dst
            for s, e in self.convert_two(source_start, source_end, map):
                q.appendleft((dest, s, e))
        print(f'Day 5 Part 2: {res}')
        return res

    def convert(self, source, map):
        for (start, range), dest_start in map.items():
            if start <= source < start + range:
                return dest_start + (source - start)
        return source
    
    def convert_two(self, source_start, source_end, map):
        ranges = [(source_start, source_end)]
        out = []
        while ranges:
            # TODO: Implement
            source_start, source_end = ranges.pop()
            found = False
            # Search through the map for the first range that overlaps the source range
            for (start, range), dest_start in map.items():
                end = start + range - 1
                if start <= source_start <= end or start <= source_end <= end:
                    if source_start < start and end < source_end:
                        out.append((dest_start, dest_start + range - 1))
                        ranges.append((source_start, start - 1))
                        ranges.append((end + 1, source_end))
                    elif source_start < start:
                        out.append((dest_start, dest_start + source_end - start))
                        ranges.append((source_start, start - 1))
                    elif end < source_end:
                        out.append((dest_start + source_start - start, dest_start + range - 1))
                        ranges.append((end + 1, source_end))
                    else:
                        out.append((dest_start + source_start - start, dest_start + source_end - start))
                    found = True
                    break
            if not found: out.append((source_start, source_end))
        
        return out



            
            
    

solver = DayFiveSolver()
solver.solve_one("day-5-sample.txt")
solver.solve_one("adventofcode-day-5-input.txt")
solver.solve_two("day-5-sample.txt")
solver.solve_two("adventofcode-day-5-input.txt")

