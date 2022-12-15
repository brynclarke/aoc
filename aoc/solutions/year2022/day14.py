from collections import deque

def solve(input_text):
    blocked = set()

    for line in input_text.strip().splitlines():
        vertices = [list(map(int, v.split(","))) for v in line.split(" -> ")]
        
        for b1, b2 in zip(vertices[:-1], vertices[1:]):
            for x in range(min(b1[0], b2[0]), max(b1[0], b2[0]) + 1):
                for y in range(min(b1[1], b2[1]), max(b1[1], b2[1]) + 1):
                    blocked.add((x, y)) # create set of blocked (rock) coords

    def move_sand(floor_level):
        sx, sy = moving_sand[-1] # only check the head

        if sy >= floor_level - 1: # can't move into floor
            return False
        elif not (sx, sy + 1) in blocked: # can move straight down
            moving_sand.append((sx, sy + 1)) # add sand at new head
        elif not (sx - 1, sy + 1) in blocked: # can move diag left
            moving_sand.append((sx - 1, sy + 1)) # add sand at new head
        elif not (sx + 1, sy + 1) in blocked: # can move diag right
            moving_sand.append((sx + 1, sy + 1)) # add sand at new head
        else: # can't move
            return False
        
        moving_sand.popleft() # pop sand at old tail (if moving, then like a snake)
        return True

    abyss = max([b[1] for b in blocked]) # lowest blocked coordinate (positive y)

    moving_sand = deque([(500, 0)]) # start with one moving sand particle
    stopped_sand = set() # start with no stopped sand partiles

    part1 = 0
    while True:
        if len(moving_sand) == 0: # all sand stopped
            break
        
        if move_sand(floor_level = abyss + 2):
            moving_sand.appendleft((500, 0)) # sand moved, add more
        else:
            s = moving_sand.pop() # sand stopped, pop head from deque
            stopped_sand.add(s) # move head to stopped set
            blocked.add(s) # add stopped sand to blocked set

        if part1 == 0 and moving_sand[-1][1] >= abyss: # first sand reached abyss
            part1 = len(stopped_sand) # stopped sand count when reach abyss

    part2 = len(stopped_sand) # stopped sand count when no more sand is moving

    return (part1, part2)
                