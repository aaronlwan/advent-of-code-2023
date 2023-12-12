from collections import Counter

class DaySevenSolver:
    def read_file(self, file_name):
        hands, bids = [], []
        with open(file_name) as file:
            for line in file:
                l = line.strip()
                hand, bid = l.split(' ')
                hands.append(hand)
                bids.append(int(bid))
        return hands, bids

    def solve(self, file_name, part=1):
        hands, bids = self.read_file(file_name)
        hand_ranks = []
        res = 0
        if part == 2: strength = 'AKQT98765432J'[::-1]
        else: strength = 'AKQJT98765432'[::-1]
        for hand in hands:
            counts = Counter(hand)
            if part == 2 and 'J' in counts:
                j_count = counts.pop('J')
                if j_count == 5: counts = {'A': 5}
                else:
                    max_key = max(counts, key=lambda x: (counts[x], strength.index(x)))
                    counts[max_key] += j_count

            tiebreaker = tuple(strength.index(card) * 10 ** (4 - i) for i, card in enumerate(hand))
            values = sorted(list(counts.values()), reverse=True)
            type = sum(val * 10 ** (4 - i) for i, val in enumerate(values))
            hand_ranks.append((type, tiebreaker))

        ranked = sorted(list(zip(hand_ranks, bids)), key=lambda x: (x[0][0], x[0][1]), reverse=True)
        for i, (_, bid) in enumerate(ranked): 
            res += (len(ranked) - i) * bid
        print(f'Day 7 Part {part} Answer: {res}')
        return res

solver = DaySevenSolver()
solver.solve('adventofcode-day-7-input.txt')
solver.solve('adventofcode-day-7-input.txt', 2)