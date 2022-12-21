def solve(input_text):
    commands = {}
    for line in input_text.strip().splitlines():
        commands[line[:4]] = line[6:].split(" ")

    def evaluate(key, humn=None):
        op = commands[key]

        if key == "humn" and humn is not None:
            return humn

        if len(op) == 1:
            return int(op[0])
        
        assert op[0] in commands and op[2] in commands

        lhs = evaluate(op[0], humn)
        rhs = evaluate(op[2], humn)

        if key == "root" and humn is None: return int(lhs + rhs) # part1
        if key == "root" and humn is not None: return lhs - rhs # part2
        if op[1] == "+": return lhs + rhs
        elif op[1] == "-": return lhs - rhs
        elif op[1] == "*": return lhs * rhs
        elif op[1] == "/": return lhs / rhs
        else: assert False

    # part1 is a simple recursive evaluation
    part1 = evaluate("root")

    # part 2 requires trial and error
    # we track the prior guess and make educated next guesses
    prior_h = None
    prior_r = None

    h = 1
    while True:
        r = evaluate("root", h)

        if r == 0:
            break

        # use a numerical method to find the next guess
        # (I think this is called Euler's technique? extend x in the direction 
        # and by the amount the slope indicates is needed to reach zero)
        if prior_h is None:
            h_est = h + 1 # basically seeding the slope
        else:
            slope = (r - prior_r) / (h - prior_h)
            # but also (assuming slope is constant)
            # slope = (goal - r) / (h_est - h)
            h_est = h + (0 - r) / slope

        prior_h, prior_r = h, r
        h = h_est

    # converged to solution
    part2 = int(h)

    return part1, part2