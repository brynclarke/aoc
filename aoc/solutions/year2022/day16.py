def solve(input_text):
    # process input lines and store in dictionary vdict
    vdict = {} # has form {'AA': 10, ['BB', 'CC']..} flow=10
    for line in input_text.strip().splitlines():
        line = line.replace("Valve ", "") \
            .replace(" has flow rate=", ",") \
            .replace("s", "") \
            .replace("; tunnel lead to valve ", ",") \
            .replace(", ", ",").split(",")
        vname, flow = line[:2]
        flow = int(flow)
        connects = set(line[2:])
        vdict[vname] = (flow, connects)

    # keep a sorted list of valve names (hereafter we will use indices from this list)
    vnames = sorted(list(vdict.keys()))
    nvalves = len(vnames)

    # postprocess graph dictionary into [(10, {1, 2})...] list format (tuples of flow/edges)
    vlist = list([None for _ in range(nvalves)])
    for vname, (flow, connects) in vdict.items():
        valve = vnames.index(vname)
        vlist[valve] = (flow, set(vnames.index(connect) for connect in connects))

    # many valves have zero flow (no point ever turning them on)
    # generate a set of 'working' valves with positive flow rates
    working = frozenset([v for v, (f, _) in enumerate(vlist) if f > 0])

    # implement shortest path in networkx (bellman-ford)
    import networkx as nx
    G = nx.Graph()
    for valve, (_, connects) in enumerate(vlist):
        for connect in connects:
            G.add_edge(valve, connect)
    paths = dict(nx.shortest_path_length(G))

    # main recursive traversal function (dynamic programming method)
    def traverse(start, time, opened, pressure, released, nworkers=1):
        global best, END
        key = (start, time, opened, pressure, released, nworkers)
        hkey = hash(key)
        if hkey in best: # 
            return best[hkey]
        
        picked = 0
        for dest in working - opened | set((None, )): # available destinations or None (worker done)
            if dest is None: # worker done opening
                outcome = released + pressure * (END - time) # pressure released from worker waiting
                if nworkers > 1: # more workers to calculate
                    outcome += traverse(0, 0, opened, 0, 0, nworkers-1)
                if outcome > picked:
                    picked = outcome
            else:
                when = time + paths[start][dest] + 1 # add travel time and 1 minute to open
                if when <= END: # have time to open
                    opened_ = opened | set((dest, ))
                    pressure_ = pressure + vlist[dest][0]
                    released_ = released + pressure * (when - time)
                    outcome = traverse(dest, when, opened_, pressure_, released_, nworkers)
                    if outcome > picked:
                        picked = outcome

        pkey = hash(picked)
        best[pkey] = picked

        return picked

    def solve(nworkers):
        global best, END
        best = {}
        END = 30 - (nworkers - 1) * 4
        return traverse(0, 0, frozenset(), 0, 0, nworkers)

    part1, part2 = [solve(w) for w in range(1, 3)]

    return part1, part2