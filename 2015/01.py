import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "01.in"
print(sys.argv[2] if len(sys.argv) > 2 else "", end="")

data = open(infile).read().strip()
#lines = data.splitlines()

part1 = 0
part2 = 0

for i, char in enumerate(data):
    if char == "(":
        part1 += 1
    else:
        assert char ==")"
        part1 -= 1

    if part2 == 0 and part1 == -1:
        part2 = i + 1

print(part1, part2)