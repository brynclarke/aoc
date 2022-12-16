#from collections import Counter
#import hashlib
#import itertools
#from copy import deepcopy
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "04.in"
print(sys.argv[2] if len(sys.argv) > 2 else "", end="")

data = open(infile).read().strip()

part1 = 0
part2 = 0
for line in data.splitlines():
    chars = []
    encoded = '"'
    i = 0
    while True:
        r = len(line) - i - 1
        char = line[i]

        if i == 0:
            encoded += '\\\"' 
            i += 1
        elif r == 0:
            encoded += '\\\"'
            break
        else:
            if char == '\\':
                encoded += '\\\\'
                next = line[i+1]
                if next == '"':
                    chars += ['"']
                    encoded += '\\\"'
                    i += 2
                elif next == '\\':
                    encoded += '\\\\'
                    chars += ['\\']
                    i += 2
                elif next == 'x':
                    encoded += line[i+1:i+4]
                    chars += [line[i+1:i+4]]
                    i += 4
            else:
                chars += char
                encoded += char
                i += 1

    encoded += '"'

    part1 += len(line) - len(chars)
    part2 += len(encoded) - len(line)

print(part1, part2)