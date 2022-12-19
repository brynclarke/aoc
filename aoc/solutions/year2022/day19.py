def solve(input_text):
    # processing manually (could use regex here)... output is list (# blueprints) of lists (# robots) of lists (# mineral types)
    BLUEPRINTS = []
    for bp_text in input_text.strip().split("\n"):
        bp = [[0, 0, 0, 0] for _ in range(4)]
        for ridx, cost_text in enumerate(bp_text.split("Each ")[1:]):
            for mat_text in cost_text.split(" costs ")[1].replace(". ", ".")[:-1].split(" and "):
                amt, mat = mat_text.split(" ")
                midx = ["ore", "clay", "obsidian", "geode"].index(mat)
                bp[ridx][midx] = int(amt)
        BLUEPRINTS += [bp]

    INCOME_CAPS = []
    for bp in BLUEPRINTS:
        # we can't spend more than these amounts each turn
        # also no point buying a robot that can only unlock buying another of the same robot
        INCOME_CAPS += [[max([bp[ridx][midx] - int(ridx == midx) for ridx in range(4)]) for midx in range(3)]]

    global DP, SIMTIME
    def simulate(state):
        # wealth tracks the amount of ore, clay, obsidian, and geodes owned
        # income prior to any new robots built this step is used to adjust wealth
        # wealth before income is used to determine which robots can be purchased this step
        # wealth is capped at the most that can be spent by the end of the simulation (improves runtime a bit)
        def wealth_after_income(old_wealth, used_income):
            wealth_plus_income = tuple(w + i for w, i in zip(old_wealth, used_income))
            expected_income = tuple(i*(SIMTIME - minute) for i in used_income[:-1])
            most_needed = tuple(WEALTH_CAP[minute][midx] - expected_income[midx] for midx in range(3))
            wealth_capped = tuple(min(wealth_plus_income[midx], most_needed[midx]) for midx in range(3)) + (wealth_plus_income[-1], )
            return wealth_capped

        global DP, SIMTIME

        # any states we've evaluated before are stored (hashed) in DP (alias for dynamic programming)
        hkey = hash(state)
        if hkey in DP:
            return DP[hkey]

        # state consists of the time (minute), wealth (ore... geode counts), and income (robot counts)
        minute, wealth, income = state
        if minute == SIMTIME: return wealth[-1] # simulation outcome (number of geodes)
        
        minute += 1
        outcomes = [] # store outcomes from each possibility (purchase one of four robots if can afford or purchase none)
        for ridx, bp in reversed(list(enumerate(BLUEPRINT))): # consider each option in blueprint
            if ridx != 3: # we always can use more geode since that's the ultimate goal 
                if income[ridx] >= INCOME_CAP[ridx]: # no point buying more of this robot
                    continue

            balances = tuple(wealth[midx] - bp[midx] for midx in range(4)) # calculate balances after purchase
            if all(w >= 0 for w in balances): # if no negative balances
                new_income = tuple(income[midx] + int(ridx == midx) for midx in range(4)) # adjust income
                outcomes.append(simulate((minute, wealth_after_income(balances, income), new_income)))

        outcomes.append(simulate((minute, wealth_after_income(wealth, income), income)))

        best = max(outcomes)
        DP[hash(state)] = best # store best outcome using hashkey in case we see this state again

        return best

    # part 1 solution: we recursively search states using DP for 24 minutes
    SIMTIME = 24

    # wealth is capped at (amt that can be spent each turn) x (# turns remaining in simulation)
    WEALTH_CAPS = []
    for bp in BLUEPRINTS:
        WEALTH_CAPS += [[[max([bp[ridx][midx]*turns for ridx in range(4)]) for midx in range(3)] for turns in range(SIMTIME + 1, -1, -1)]]

    part1 = 0
    for bidx, BLUEPRINT in enumerate(BLUEPRINTS):
        INCOME_CAP = INCOME_CAPS[bidx] # most we would want to earn of each type
        WEALTH_CAP = WEALTH_CAPS[bidx] # most we could possibly spend of each type
        DP = {}
        initial_state = (
            0, # minute
            (0, 0, 0, 0), # wealth (ore/clay/obsidian/geode)
            (1, 0, 0, 0) # income (ore/clay/obsidian/geode)
        )
        part1 += simulate(initial_state) * (bidx + 1) # compute "quality" of blueprint (geodes x ID) and accumuluate

    # part 2 solution: we recursively search states using DP for 32 minutes (but only 3 blueprints)
    SIMTIME = 32

    # wealth caps need to be recalculated for the longer simulation times
    WEALTH_CAPS = []
    for bp in BLUEPRINTS:
        WEALTH_CAPS += [[[max([bp[ridx][midx]*turns for ridx in range(4)]) for midx in range(3)] for turns in range(SIMTIME + 1, -1, -1)]]

    part2 = 1
    for bidx, BLUEPRINT in enumerate(BLUEPRINTS[:3]): # only 3 blueprints
        INCOME_CAP = INCOME_CAPS[bidx] # most we would want to earn of each type
        WEALTH_CAP = WEALTH_CAPS[bidx] # most we could possibly spend of each type

        DP = {}
        initial_state = (
            0, # minute
            (0, 0, 0, 0), # wealth (ore/clay/obsidian/geode)
            (1, 0, 0, 0) # income (ore/clay/obsidian/geode)
        )
        part2 *= simulate(initial_state) # just accumulate product of geodes

    return part1, part2
        