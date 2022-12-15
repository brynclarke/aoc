import itertools
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "02.in"
print(sys.argv[2] if len(sys.argv) > 2 else "", end="")

data = open(infile).read().strip()

part1 = 0
part2 = 0

for line in data.splitlines():
    dims = list(map(int, line.split("x")))
    sides = list(itertools.combinations(dims, 2))
    areas = [a*b for a, b in sides]
    perims = [2*(a + b) for a, b in sides]

    bow = 1
    for d in dims:
        bow *= d

    part1 += 2 * sum(areas) + min(areas)
    part2 += min(perims) + bow

print(part1, part2)