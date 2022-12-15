def solve(input_text):
    data = []
    for line in input_text.splitlines():
        line = line.replace("Sensor at x=", "") \
            .replace(", y=", ",") \
            .replace(": closest beacon is at x=", ",")
        data.append(list(map(int, line.split(","))))

    def manhattan(a, b):
        return abs(a.real - b.real) + abs(a.imag - b.imag)

    # populate sensors as dict key=coord tuple in complex plane, value=dist to nearest beacon
    # populate beacons as set of complex coords
    sensors = {}
    beacons = set()
    for sx, sy, bx, by in data:
        scoord = sx + sy * 1j
        bcoord = bx + by * 1j
        dist = manhattan(scoord, bcoord)
        sensors[scoord] = dist
        beacons.add(bcoord)

    # helper function to return blocked coords in a given row (y-value)
    def horizontal_scan(k):
        segments = []

        for s, d in sensors.items():
            if s.imag - d <= k <= s.imag + d: # sensor diamond has some intersection at line y=k
                d_vert = abs(k - s.imag) # vertical distance of sensor to line y=k
                d_horz = d - d_vert # remaining (horizontal) distance (boundaries will be at +/- in x)
                lbound = int(s.real - d_horz) # left boundary of intersection
                rbound = int(s.real + d_horz) # right boundary of intersection

                segments.append([lbound, rbound])

        segments = sorted(segments)
        merged = []
        i = 0
        for seg in segments:
            if len(merged) == 0: # first segment
                merged.append(seg)
            else: 
                assert seg[0] >= merged[-1][0] # since sorted
                if seg[0] <= merged[-1][1]: # overlaps
                    merged[-1][1] = max(merged[-1][1], seg[1]) # keep lbound, use highest rbound
                else:
                    merged.append(seg) # discontinuous
                    
        return merged

    # PART 1
    y = 2_000_000 if len(sensors) >= 15 else 10 # minor difference in test vs. submission data
    p1_segments = horizontal_scan(y)

    # count sensors and beacons along horizontal line at y
    n_sensors = n_beacons = 0
    for s, d in sensors.items():
        if s.imag == y:
            for seg in p1_segments:
                if seg[0] <= s.real <= seg[1]: # sensor s falls in segment seg
                    n_sensors += 1
                    break

    for b in beacons:
        if b.imag == y:
            for seg in p1_segments:
                if seg[0] <= b.real <= seg[1]: # beacon b falls in segment seg
                    n_beacons += 1
                    break

    # possible positions is (inclusive) sum of segments less # sensors/beacons
    part1 = sum([s[1] - s[0] + 1 for s in p1_segments]) - n_sensors - n_beacons

    # PART 2
    ymin, ymax = 0, 4_000_000 # range of y values to look for possible sensor

    for y in range(ymin, ymax):
        p2_segments = horizontal_scan(y) # get segments of impossible x values

        if len(p2_segments) > 1: # segments are discontinuous
            assert len(p2_segments) == 2 # only one possible result (single discontinuity)
            assert p2_segments[0][1] + 1 == p2_segments[1][0] - 1 # only one open x value
            x = p2_segments[0][1] + 1 # open x position between 1st and 2nd segments
            part2 = x*4000000 + y # tuning frequency formula provided
            break

    return part1, part2
                