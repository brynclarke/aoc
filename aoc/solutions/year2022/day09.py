def solve(input_text):
    commands = [line.split(" ") for line in input_text.splitlines()]
    part_answers = []

    for rope_length in [2, 10]:
        tail_visits = []

        # list of tuples stores rope unit coordinates (0=lead)
        rope = [(0, 0), ] * rope_length

        for (dir, dist) in commands:
            # mx, my = movement of lead rope unit
            if dir == "L":
                mx, my = -1, 0
            elif dir == "R":
                mx, my = 1, 0
            elif dir == "U":
                mx, my = 0, 1
            elif dir == "D":
                mx, my = 0, -1
            
            # move input distance units (one by one)
            for _ in range(int(dist)):
                # move lead rope unit in calculated direction
                rope[0] = (rope[0][0] + mx, rope[0][1] + my)

                for i in range(1, len(rope)):
                    # tx, ty = distance to next rope unit
                    tx = rope[i][0] - rope[i-1][0]
                    ty = rope[i][1] - rope[i-1][1]

                    # dx, dy = movement toward next rope unit
                    dx = 0
                    dy = 0

                    if max(abs(tx), abs(ty)) >= 2:
                        # only move if at least 2 away in one direction
                        if tx == 0:
                            # move one unit vertically
                            dy = -int(ty/abs(ty))
                        elif ty == 0:
                            # move one unit horizontally
                            dx = -int(tx/abs(tx))
                        else:
                            # move diagonally
                            dx = -int(tx/abs(tx))
                            dy = -int(ty/abs(ty))

                    # move rope unit
                    rope[i] = (rope[i][0] + dx, rope[i][1] + dy)

                # add coordinates to tail visit list
                tail_visits.append(rope[-1])
        
        part_answers += [len(set(tail_visits))]

    # (part1, part2)
    return tuple(part_answers)