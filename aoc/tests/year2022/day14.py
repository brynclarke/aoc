from aoc.solutions.year2022.day14 import solve

def unit_test():
    input_text = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    solution = solve(input_text)
    expected_solution = (24, 93)

    assert solution == expected_solution