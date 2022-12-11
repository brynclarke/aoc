def solve(input_text):
    input_lines = input_text.splitlines()
    operations = [line.split(" ") for line in input_lines]

    # cycle tracks number of cycles started
    # e.g. cycle increments to 1 at the start of the 1st cycle
    # cycle remains 1 during and at the end of the 1st cycle
    cycle = 0
    X = 1
    global ss, img_lines
    ss = []
    img_lines = []

    def during_cycle():
        global ss, img_lines

        # update pixel every cycle (1..40)
        pixel_x = (cycle - 1) % 40 + 1

        # update signal strength if pixel 20 (cycle 20, 60...)
        if pixel_x == 20:
            ss += [(cycle)*X]
        # add new line if pixel 1 (first pixel in line)
        elif pixel_x == 1:
            img_lines += [""]    

        # draw lit pixel if X w/in one either direction
        if abs(X - (pixel_x - 1)) <= 1:
            img_lines[-1] += "█"
        # otherwise draw unlit pixel
        else:
            img_lines[-1] += " "

    for op in operations:
        # set number of cycles for operation
        if op[0] == "noop":
            op_cycles = 1
        elif op[0] == "addx":
            op_cycles = 2
        else:
            raise ValueError
        
        # loop through cycles calling `during_cycle`
        for _ in range(op_cycles):
            cycle += 1
            during_cycle()
        
        # end of operation (update X on addx ops)
        if op[0] == "noop":
            pass
        elif op[0] == "addx":
            X += int(op[1])
        else:
            raise ValueError

    part1 = sum(ss[:6])
    part2 = "\n".join("".join(ln) for ln in img_lines)

    return part1, part2