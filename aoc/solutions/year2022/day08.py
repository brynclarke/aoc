def solve(input_text):
    w = input_text.index("\n")
    h = int(len(input_text) / (w + 1))

    part1 = 0
    m = {}

    for i in range(h): # row
        for j in range(w): # col
            m[(i, j)] = [0, 0, 0, 0]
            t1 = input_text[i*(w+1) + j]

            vis_left = True
            for k in range(j-1, -1, -1):
                t2 = input_text[i*(w+1) + k]

                # tree left
                m[(i, j)][0] += 1

                if int(t2) >= int(t1):
                    vis_left = False
                    # not vis left
                    break

            vis_right = True
            for k in range(j+1, w):
                t2 = input_text[i*(w+1) + k]

                # tree right
                m[(i, j)][1] += 1

                if int(t2) >= int(t1):
                    vis_right = False
                    # not vis right
                    break

            vis_top = True
            for k in range(i-1, -1, -1):
                t2 = input_text[k*(w+1) + j]

                # tree top
                m[(i, j)][2] += 1

                if int(t2) >= int(t1):
                    vis_top = False
                    # not vis top
                    break

            vis_bot = True
            for k in range(i+1, h):
                t2 = input_text[k*(w+1) + j]

                # tree bot
                m[(i, j)][3] += 1

                if int(t2) >= int(t1):
                    vis_bot = False
                    # not vis bot
                    break

            if vis_left or vis_right or vis_top or vis_bot:
                part1 += 1

    scenic_scores = []
    for dir_score in m.values():
        score = 1
        for s in dir_score:
            score *= s
        scenic_scores += [score]    

    part2 = max(scenic_scores)

    return (part1, part2)