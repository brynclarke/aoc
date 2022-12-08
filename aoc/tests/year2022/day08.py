from aoc.solutions.year2022.day08 import solve

def unit_test():
    input_text = \
"""30373
25512
65332
33549
35390
"""

    solution = solve(input_text)
    expected_solution = (21, 8)

    assert solution == expected_solution