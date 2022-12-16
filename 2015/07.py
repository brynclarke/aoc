#from collections import Counter
#import hashlib
#import itertools
from copy import deepcopy
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "04.in"
print(sys.argv[2] if len(sys.argv) > 2 else "", end="")

data = open(infile).read().strip()

operations = {}
for line in  data.splitlines():
    lhs, rhs = line.split(" -> ")
    lhs = lhs.split(" ")
    
    if len(lhs) == 1:
       if lhs[0].isdigit():
           operations[rhs] = (None, int(lhs[0]), None)
       else:
           operations[rhs] = (None, lhs[0], None)
    elif len(lhs) == 2:
        assert lhs[0] == "NOT"
        operations[rhs] = (lhs[0], lhs[1], None)
    else:
        assert len(lhs) == 3
        operations[rhs] = (lhs[1], lhs[0], lhs[2])

def evaluate(key):
    if isinstance(key, int): val = key
    elif key.isdigit(): val = int(key)
    else:
        op = operations[key]
        
        val = evaluate(op[1])    
        if op[0] is None: pass
        elif op[0] == "NOT": val ^= 0xffff
        else:
            b = evaluate(op[2])
            if op[0] == "AND": val &= b
            elif op[0] == "OR": val |= b
            elif op[0] == "LSHIFT": val <<= b
            elif op[0] == "RSHIFT": val >>= b
            else:
                assert False, op[0]
    
        operations[key] = (None, val, None)
    return val

operations_ = deepcopy(operations)
if "a" in operations:
    part1 = evaluate("a")
else:
    part1 = evaluate("f")

operations = deepcopy(operations_)
if "a" in operations:
    operations["b"] = (None, part1, None)
    part2 = evaluate("a")
else:
    operations["x"] = (None, part1, None)
    part2 = evaluate("f")

print(part1, part2)