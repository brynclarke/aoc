def solve(input_text):
    # def visualize():
    #     """
    #     console visualization of the chamber map
    #     useful for debugging but no function in solution
    #     """

    #     if rested:
    #         chamber_height = h + 1
    #     else:
    #         chamber_height = int(max([h] + [p.imag for p in rock])) + 1
        
    #     for r in reversed(range(chamber_height)):
    #         line = ""
    #         for c in range(1, 8):
    #             if (c + r*1j) in C:
    #                 line += "#"
    #             elif (not rested) and (c + r*1j) in rock:
    #                 line += "@"
    #             else:
    #                 line += "."
    #         print(line)

    #     print()

    def process_rock_spec(rspec):
        """
        Inputs
        'rspec' (string) rock specification, e.g. "..#\n..#\n###"

        Outputs (set -> complex)
        coordinates of all locations occupied by rock with given string spec
        real coordinate is horizontal (x) position (relative to rock left)
        imaginary coordinate is vertical (y) position (relative to rock bottom)
        """

        rock_coords = set()
        for r, line in enumerate(reversed(rspec.split("\n"))):
            for c, char in enumerate(line):
                if char == "#":
                    rock_coords.add(c + r*1j)
        return rock_coords

    rock_spec = "####\n\n.#.\n###\n.#.\n\n..#\n..#\n###\n\n#\n#\n#\n#\n\n##\n##"

    # list of rocks to sample (elements are initial occupied coordinates)
    rock_list = list(map(process_rock_spec, (rock_spec.split("\n\n"))))

    # list of wind movements to sample (elements are horizontal movement 1 or -1)
    wind_list = list(map(lambda c: 1 if c == ">" else -1, input_text))

    # initialization parameters
    rock_idx = 0
    wind_idx = 0
    h = 0
    rocks = 0
    N_ROCKS = 1_000_000_000_000

    # set of occupied coordinates within the chamber
    C = set([i + 0j for i in range(1, 8)])

    def rock_collision(shift=(0 + 0j)):
        """
        Inputs
        'shift' (complex) vector to move rock before checking for collision

        Outputs (bool)
        indicator of whether the rock collides (overlaps) with the
        settled rock or floor in the chamber or the side walls
        """

        for e in rock:
            if not(1 <= (e + shift).real <= 7) or e + shift in C:
                return True
        
        return False

    memory = {}
    part1 = part2 = 0
    while True:
        if rocks == 2022:
            part1 = h

        elif rocks > 2022:
            # dynamic programming using rock and wind cycles
            config_key = (rock_idx, wind_idx)
            if config_key in memory:
                prior_rocks, prior_h = memory[config_key]

                delta_rocks = rocks - prior_rocks
                delta_h = h - prior_h

                remain_rocks = N_ROCKS - rocks
                remain_cycles = int(remain_rocks // delta_rocks)

                if remain_rocks % delta_rocks == 0:
                    remain_h = delta_h * remain_cycles
                    part2 = h + remain_h
                    break
            else:
                memory[config_key] = rocks, h

        # choose a rock
        rested = False
        rock = rock_list[rock_idx]
        rock_idx += 1
        rock_idx %= len(rock_list)
        rocks += 1

        # set initial coordinates
        rock = {e + 3 + (h + 4) * 1j for e in rock}
        #visualize()
        
        while not rested:
            # simulate wind
            wind = wind_list[wind_idx]
            wind_idx += 1
            wind_idx %= len(wind_list)
            
            if not rock_collision(shift=wind):
                rock = {e + wind for e in rock}
            #visualize()

            # simulate falling or come to rest
            if rock_collision(shift=(0 - 1j)):
                rested = True
                C |= rock
                h = int(max([h] + [p.imag for p in rock]))
            else:
                rock = {e - 1j for e in rock}
            #visualize()

    return part1, part2