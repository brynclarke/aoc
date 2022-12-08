import numpy as np

def solve(input_text):
    part1 = 0
    part2 = 0

    arr = np.array([[int(x) for x in line] for line in input_text.split()])

    for (tr, tc), tree_height in np.ndenumerate(arr):
        trees_left = arr[tr, :tc][::-1]
        trees_right = arr[tr, tc+1:]
        trees_above = arr[:tr, tc][::-1]
        trees_below = arr[tr+1:, tc]

        tree_visible = \
            np.all(trees_left < tree_height) or \
            np.all(trees_right < tree_height) or \
            np.all(trees_above < tree_height) or \
            np.all(trees_below < tree_height)
        
        def viewing_distance(trees):
            trees_in_view = trees[:np.argmax(np.hstack([
                False,
                trees >= tree_height,
                True
            ]))]

            return len(trees_in_view)

        scenic_score = np.prod([
            viewing_distance(trees) for trees in [
                trees_left, trees_right, trees_above, trees_below
            ]
        ])

        if tree_visible: part1 += 1
        part2 = max(part2, scenic_score)

    return (part1, part2)