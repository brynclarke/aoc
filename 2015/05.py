from collections import Counter
#import hashlib
#import itertools
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "04.in"
print(sys.argv[2] if len(sys.argv) > 2 else "", end="")

data = open(infile).read().strip()

part1 = 0
part2 = 0
for line in data.splitlines():
    letters = Counter(line)
    check1 = sum([v for k, v in letters.items() if k in list("aeiou")]) >= 3
    
    letters2 = Counter(map(lambda x: "".join(x), zip(line[:-1], line[1:])))
    check2 = len([k for k in letters2.keys() if k[0] == k[1]]) > 0
    check3 = len([k for k in letters2.keys() if k in "ab,cd,pq,xy".split(",")]) == 0

    if check1 and check2 and check3:
        part1 += 1

    check4 = False
    for i in range(len(line) - 1):
        left2 = line[i:i+2]
        for j in range(i+2, len(line) - 1):
            right2 = line[j:j+2]
            if left2 == right2:
                check4 = True

    letters3 = Counter(map(lambda x: "".join(x), zip(line[:-2], line[1:-1], line[2:])))
    check5 = len([k for k in letters3.keys() if k[0] == k[2] and k[0] != k[1]]) > 0

    if check4 and check5:
        part2 += 1

print(part1, part2)