#import itertools
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "03.in"
print(sys.argv[2] if len(sys.argv) > 2 else "", end="")

data = open(infile).read().strip()

# part1, part2
houses = [set(), set()]

# part1, part2 santa, part2 robo
pos = [0 + 0j, 0 + 0j, 0 + 0j]
for pt, idx in zip([0, 1, 1], [0, 1, 2]):
    houses[pt].add(pos[idx])

for i, char in enumerate(data):
    pt2 = i % 2

    for pt, idx in enumerate([0, pt2]):
        if char == "^":
            pos[pt + idx] += 1j
        elif char == ">":
            pos[pt + idx] += 1
        elif char == "v":
            pos[pt + idx] -= 1j
        elif char == "<":
            pos[pt + idx] -= 1

        houses[pt].add(pos[pt + idx])

part1 = len(houses[0])
part2 = len(houses[1])

print(part1, part2)