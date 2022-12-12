def solve(input_text):
    from collections import defaultdict
    import heapq

    grid = [[char for char in line] for line in input_text.splitlines()]

    R, C = len(grid), len(grid[0])
    S, E = None, None

    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                S = (r, c)
                grid[r][c] = "a"
            elif grid[r][c] == "E":
                E = (r, c)
                grid[r][c] = "z"
            
            grid[r][c] = ord(grid[r][c]) - ord("a")

    part1 = None
    part2 = 1e9
    for S_ in [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 0]:
        Q = [(0, S_, 0)]
        V = set()

        while Q:
            cost, P, H = heapq.heappop(Q)
            if P == E:
                if S_ == S: part1 = cost
                part2 = min(cost, part2)
                break
            if P in V: continue
            V.add(P)
            for NP in [(P[0] - 1, P[1]), (P[0] + 1, P[1]), (P[0], P[1] - 1), (P[0], P[1] + 1)]:
                if (not(0 <= NP[0] < R)) or (not(0 <= NP[1] < C)): continue
                if NP in V: continue
                NH = grid[NP[0]][NP[1]]
                if NH > H + 1: continue
                heapq.heappush(Q, (cost + 1, NP, NH))

    return (part1, part2)