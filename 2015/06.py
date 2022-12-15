#from collections import Counter
#import hashlib
#import itertools
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "04.in"
print(sys.argv[2] if len(sys.argv) > 2 else "", end="")

data = open(infile).read().strip()

N = 1000
# PART 1
lights = [[-1 for _ in range(N)] for _ in range(N)]

for line in data.splitlines():
    switch, xa, ya, xb, yb = list(map(int,line.replace(" through ", ",") \
        .replace("toggle ", "0,") .replace("turn off ", "-1,") \
        .replace("turn on ", "1,").split(",")))
    
    x1, x2 = sorted([xa, xb])
    y1, y2 = sorted([ya, yb])

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if switch == 0:
                lights[x][y] *= -1
            else:
                lights[x][y] = switch

part1 = 0
for x in range(N):
    for y in range(N):
        part1 += (lights[x][y] == 1)

# PART 2
lights = [[0 for _ in range(N)] for _ in range(N)]

for line in data.splitlines():
    switch, xa, ya, xb, yb = list(map(int,line.replace(" through ", ",") \
        .replace("toggle ", "0,") .replace("turn off ", "-1,") \
        .replace("turn on ", "1,").split(",")))
    
    x1, x2 = sorted([xa, xb])
    y1, y2 = sorted([ya, yb])

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if switch == 0:
                lights[x][y] += 2
            elif switch == 1:
                lights[x][y] += 1
            elif switch == -1:
                lights[x][y] = max(lights[x][y] - 1, 0)

part2 = 0
for x in range(N):
    for y in range(N):
        part2 += lights[x][y]

print(part1, part2)