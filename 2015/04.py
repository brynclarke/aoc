import hashlib
#import itertools
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "04.in"
print(sys.argv[2] if len(sys.argv) > 2 else "", end="")

data = open(infile).read().strip()

def test_hash(key, num, zeros):
    hash = hashlib.md5(f"{key}{str(num)}".encode())
    leading = hash.hexdigest()[:zeros]
    if leading == "0" * zeros:
        return True
    else:
        return False

part1 = 0
while True:
    part1 += 1
    if test_hash(data, part1, 5):
        break

part2 = part1 - 1
while True:
    part2 += 1
    if test_hash(data, part2, 6):
        break

print(part1, part2)