from aoc.solutions.year2022.day09 import solve

def unit_test():
    input_text = \
"""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

    solution = solve(input_text)
    expected_solution = (13, 1)

    assert solution == expected_solution