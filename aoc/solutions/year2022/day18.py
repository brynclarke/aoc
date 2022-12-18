def solve(input_text):
    import networkx as nx

    data = [[int(v) for v in line.split(",")] for line in input_text.splitlines()]

    dataset = set(tuple(pt) for pt in data)

    # define bounds of rectangular prism that has at least one unit of open air around the lava
    box_bounds = [range(min([n[i] for n in dataset]) - 1, max([n[i] for n in dataset]) + 2) for i in range(3)]

    # find air nodes (within prism boundaries but not in lava)
    air_nodes = set()
    for x in box_bounds[0]:
        for y in box_bounds[1]:
            for z in box_bounds[2]:
                u = tuple((x, y, z))
                if u not in dataset:
                    air_nodes.add(u)

    # list to help iterate quickly across 3 dimensions
    DXDYDZ = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    # define graph to hold all air to air edges
    G = nx.Graph()
    for u in air_nodes:
        for dx, dy, dz in DXDYDZ:
            v = tuple((u[0] + dx, u[1] + dy, u[2] + dz))
            if v in air_nodes:
                G.add_edge(u, v)

    # find "open" nodes (air nodes that connect to the outside)
    # origin (one of the corners of the air prism) used to find paths
    open_nodes = set()
    v = tuple(box_bounds[i][0] for i in range(3))
    for u in air_nodes:
        try:
            p = nx.shortest_path(G, u, v)
            # line above throws error if no path
            # no error so path found - node is open air
            open_nodes.add(u)
        except:
            continue

    part1 = 0
    part2 = 0
    for x, y, z in dataset:
        for dx, dy, dz in DXDYDZ:
            u = tuple((x + dx, y + dy, z + dz))
            # part 1 requires only that the adjacent node is not lava
            part1 += int(u not in dataset)
            # part 2 requires that the adjacent node is open air
            part2 += int(u in open_nodes)

    return part1, part2